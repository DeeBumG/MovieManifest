from django.shortcuts import render
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from .models import Ticker

def home(request):
    return render(request, 'BiotechBin/home.html', {'title': 'Home'})

def manage_settings(request):
    return render(request, 'BiotechBin/manage_settings.html', {'title': 'manage_settings'})

def view_reccommendations(request):
    return render(request, 'BiotechBin/view_reccommendations.html', {'title': 'view_reccommendations'})

def preferences(request):
    genres = ['Action', 'Adventure', 'Animation', 'Biography', 'Comedy', 'Crime',
        'Documentary', 'Drama', 'Family', 'Fantasy', 'Film-Noir', 'Game-Show',
        'History', 'Horror', 'Music', 'Musical', 'Mystery', 'News',
        'Reality-TV', 'Romance', 'Sci-Fi', 'Sport', 'Talk-Show', 'Thriller',
        'War', 'Western']
    if request.method == 'POST':
        selected_genres = request.POST.getlist('genres')
        # Save to user profile or session
        print(selected_genres)  # Debug or store
    return render(request, 'BiotechBin/preferences.html', {'genres': genres})

def custom_logout(request):
    logout(request)
    return HttpResponseRedirect('/')