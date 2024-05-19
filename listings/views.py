from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Listing, Job, Company
from .forms import ListingForm, JobForm, CompanyForm
from accounts.models import MyUser

# Create Listings
class ListingCreateView(CreateView):
    model = Listing
    form_class = ListingForm
    template_name = 'listings/listing_create.html'
    success_url = reverse_lazy('listings')

# Get listings
class ListingListView(ListView):
    model = Listing
    template_name = 'listings/listing_list.html'
    context_object_name = 'listings'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('-listing_date')

# Get listing
class ListingDetailView(DetailView):
    model = Listing
    template_name = 'listings/listing_detail.html'
    context_object_name = 'listing'

# Update listing
class ListingUpdateView(UpdateView):
    model = Listing
    form_class = ListingForm
    template_name = 'listings/listing_update.html'
    success_url = 'listings'  

# Delete listing
class ListingDeleteView(DeleteView):
    model = Listing
    template_name = 'listings/listing_delete.html'
    success_url = 'listings'  


# the search
def search_results(request):
    query = request.GET.get('query')
    search_by = request.GET.get('search_by')

    if search_by == 'listing':
        listings = Listing.objects.filter(name__icontains=query)
        context = {'listings': listings, 'query': query, 'search_by': search_by}
        return render(request, 'accounts/search_results.html', context)
    elif search_by == 'user':
        users = MyUser.objects.filter(email__icontains=query)
        context = {'users': users, 'query': query, 'search_by': search_by}
        return render(request, 'accounts/search_results.html', context)
    else:
        return render(request, 'invalid_search_criteria.html')
    
# jobs
class JobCreateView(CreateView):
    model = Job
    form_class = JobForm
    template_name = 'listings/job_create.html'
    success_url = reverse_lazy('jobs')

# get all jobs
class JobsListView(ListView):
    model = Job
    template_name = 'listings/jobs.html'
    context_object_name = 'jobs'
    ordering = ['-listed_date']

# company
class CompanyCreateView(CreateView):
    model = Company
    form_class = CompanyForm
    template_name = 'company/company_create.html'
    success_url = reverse_lazy('jobs')

# Update company profile
class CompanyUpdateView(UpdateView):
    model = Company
    form_class = CompanyForm
    template_name = 'company/company_update.html'
    
    def get_success_url(self):
        return reverse_lazy('dashboard', args=[self.request.user.id])