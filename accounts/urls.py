from django.urls import path
# fix my imports for views
from .views import SignUpView, logout_view, login, profile
from . import views

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', login, name='login'),
    path('profile/<int:user_id>', profile, name='profile'),
    path('logout/', logout_view, name='logout'),
    path('download/<int:cv_id>/', views.download_cv, name='download_cv'),
]
