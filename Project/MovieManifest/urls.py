from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.home, name='home'),
    path('manage_settings/', views.manage_settings, name='manage_settings'),
    path('view_reccommendations/', views.view_reccommendations, name='view_reccommendations'),
    path('preferences/', views.preferences, name='preferences'),
    path('login/', LoginView.as_view(template_name='MovieManifest/login.html'), name='login'),
    path('register/', LoginView.as_view(template_name='MovieManifest/register.html'), name='register'),
    path('logout/', views.custom_logout, name='logout'),
]