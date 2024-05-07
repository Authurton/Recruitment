from django.urls import path
from .views import (
    ListingCreateView,
    ListingListView,
    ListingDetailView,
    ListingUpdateView,
    ListingDeleteView,
    search_results,
)

urlpatterns = [
    path('create/', ListingCreateView.as_view(), name='listing_create'),
    path('', ListingListView.as_view(), name='listings'),
    path('<int:pk>/', ListingDetailView.as_view(), name='listing_detail'),
    path('<int:pk>/update/', ListingUpdateView.as_view(), name='listing_update'),
    path('<int:pk>/delete/', ListingDeleteView.as_view(), name='listing_delete'),
    path('search-results', search_results, name='search_results'),
]
