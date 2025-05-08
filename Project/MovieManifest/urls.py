from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('manage_settings/', views.manage_settings, name='manage_settings'),
    path('view_reccommendations/', views.view_reccommendations, name='view_reccommendations'),
    path('preferences/', views.preferences, name='preferences'),
    path('movie/<int:pk>/', views.movie_detail_view, name='movie_detail'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', views.custom_logout, name='logout'),

]