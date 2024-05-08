from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib import messages, auth
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.conf import settings
import os
from django.db.models import Q

from .forms import SignInForm, SignUpForm
from .models import MyUser
from .models import CV 


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'accounts/signup.html'

    def form_valid(self, form):
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy('listings') 

def login(request):
    if request.method == 'POST':
      email = request.POST['email']
      password = request.POST['password']

      user = auth.authenticate(email=email, password=password)
      if user is not None:
              auth.login(request, user)
              return redirect("listings")
      else:
              messages.error(request, 'Invalid credentials')
              return redirect('login')

    else:
        return render(request, 'accounts/login.html')
    

def logout_view(request):
  logout(request)
  return HttpResponseRedirect(reverse_lazy('login')) 

# login then can access the profile
def profile(request, user_id):
    user_profile = MyUser.objects.get(id=user_id)
    if request.method == 'POST':
        cv_file = request.FILES.get('cv_file')
        if cv_file:
            cv = CV.objects.create(user=request.user, cv_file=cv_file)
            return redirect('profile', user_id=user_id) 

    cv_data = CV.objects.filter(user=user_profile).order_by('-uploaded_at')  
    context ={
        'user_profile': user_profile,
        'cv_data': cv_data,
    }
    return render(request, 'accounts/profile.html', context) 

def download_cv(request, cv_id):
    cv_instance = CV.objects.get(pk=cv_id)
    cv_path = os.path.join(settings.MEDIA_ROOT, cv_instance.cv_file.name)
    with open(cv_path, 'rb') as f:
        response = HttpResponse(f.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename=' + os.path.basename(cv_path)
        return response

# else if hiring can have a dashboard to see contacted candidates
def recruiter_dashboard(request, user_id):
    recruiter = MyUser.objects.get(Q(id=user_id) & Q(is_recruiter = True))
    
    context = {
        'recruiter': recruiter,
    }
    return render(request, 'accounts/dashboard.html', context)
# can finish their details(company)
# can reject or accept

