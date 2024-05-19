from django.urls import path
from .views import (
    ListingCreateView,
    ListingListView,
    ListingDetailView,
    ListingUpdateView,
    ListingDeleteView,
    search_results,
    JobCreateView,
    CompanyCreateView,
    JobsListView
)

urlpatterns = [
    path('create/', ListingCreateView.as_view(), name='listing_create'),
    path('', ListingListView.as_view(), name='listings'),
    path('<int:pk>/', ListingDetailView.as_view(), name='listing_detail'),
    path('<int:pk>/update/', ListingUpdateView.as_view(), name='listing_update'),
    path('<int:pk>/delete/', ListingDeleteView.as_view(), name='listing_delete'),
    path('search-results', search_results, name='search_results'),

    # jobs
    path('job-create/', JobCreateView.as_view(), name='job_create'),
    path('jobs', JobsListView.as_view(), name='jobs'),

    # company
    path('company-create/', CompanyCreateView.as_view(), name='company_create'),

]
