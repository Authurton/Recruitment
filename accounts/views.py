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
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.http import FileResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .forms import SignInForm, SignUpForm
from .models import MyUser
from .models import CV, CVView 
from listings.models import Job


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

def profile(request, user_id):
    user_profile = get_object_or_404(MyUser, id=user_id)

    if request.method == 'POST':
        cv_file = request.FILES.get('cv_file')
        if cv_file:
            CV.objects.create(user=request.user, cv_file=cv_file)
        return redirect('profile', user_id=user_id)

    cv_data = user_profile.cv_set.select_related('user').order_by('-uploaded_at')
    cv_views = CVView.objects.filter(cv__user=user_profile).order_by('-created_at')

    paginator = Paginator(cv_views, 5) 
    page = request.GET.get('page')

    try:
        cv_views_paginated = paginator.page(page)
    except PageNotAnInteger:
        cv_views_paginated = paginator.page(1)
    except EmptyPage:
        cv_views_paginated = paginator.page(paginator.num_pages)

    context = {
        'user_profile': user_profile,
        'cv_data': cv_data,
        'views': cv_views_paginated,
    }

    return render(request, 'accounts/profile.html', context)

def download_cv(request, cv_id, user_id, request_user_id):
    cv_instance = get_object_or_404(CV, pk=cv_id, user_id=user_id)
    viewed_user = cv_instance.user

    if not viewed_user.cv_views:
        viewed_user.cv_views = True
        viewed_user.save()

    CVView.objects.create(cv=cv_instance, viewer_id=request_user_id)

    cv_path = cv_instance.cv_file.path
    response = FileResponse(open(cv_path, 'rb'), content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="{cv_instance.cv_file.name}"'
    return response

# else if hiring can have a dashboard to see contacted candidates
def recruiter_dashboard(request, user_id):
    recruiter = MyUser.objects.get(Q(id=user_id) & Q(is_recruiter = True))
    user_jobs = Job.objects.filter(id=user_id)
    
    context = {
        'recruiter': recruiter,
        'jobs': user_jobs,
    }
    return render(request, 'accounts/dashboard.html', context)
# can finish their details(company)
# can reject or accept

