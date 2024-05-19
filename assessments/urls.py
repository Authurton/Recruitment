from django.urls import path
from . import views

urlpatterns = [
    path('assessments/', views.all_assessments, name='assess'),
]
