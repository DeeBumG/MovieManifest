from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from .models import SiteSetting
from .forms import SiteSettingFormSet

def home(request):
    popular_movies = [
        {'id': 1, 'title': 'Dune: Part Two', 'image_url': 'https://m.media-amazon.com/images/M/MV5BNTc0YmQxMjEtODI5MC00NjFiLTlkMWUtOGQ5NjFmYWUyZGJhXkEyXkFqcGc@._V1_.jpg'},
        {'id': 2, 'title': 'Oppenheimer', 'image_url': 'https://m.media-amazon.com/images/M/MV5BN2JkMDc5MGQtZjg3YS00NmFiLWIyZmQtZTJmNTM5MjVmYTQ4XkEyXkFqcGc@._V1_.jpg'},
        # Add more...
    ]

    recommended_movies = [
        {'id': 5, 'title': 'Arrival'},
        {'id': 6, 'title': 'Ex Machina'},
    ]

    return render(request, 'MovieManifest/home.html', {
        'popular_movies': popular_movies,
        'recommended_movies': recommended_movies
    })

def manage_settings(request):
    # Fake settings data
    settings_data = [
        {'key': 'site_name', 'value': 'MovieManifest'},
        {'key': 'enable_recommendations', 'value': 'True'},
        {'key': 'maintenance_mode', 'value': 'False'},
    ]

    return render(request, 'MovieManifest/manage_settings.html', {'settings_data': settings_data})

def view_reccommendations(request):
    return render(request, 'MovieManifest/view_reccommendations.html', {'title': 'view_reccommendations'})

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
    return render(request, 'MovieManifest/preferences.html', {'genres': genres})
def movie_detail_view(request, pk):
    return render(request, 'movie_detail.html', {'movie_id': pk})


def custom_logout(request):
    logout(request)
    return HttpResponseRedirect('/')