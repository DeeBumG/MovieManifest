from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from .models import SiteSetting
from .forms import SiteSettingFormSet

def home(request):
    popular_movies = [
        {'id': 1, 'title': 'Nacho Libre', 'image_url': 'https://m.media-amazon.com/images/M/MV5BMjMyNmEzNWYtMDNkYS00NGFmLWE3YjYtNDViYjUyMDA3MTlkXkEyXkFqcGc@._V1_.jpg'},
        {'id': 2, 'title': 'School of Rock', 'image_url': 'https://m.media-amazon.com/images/M/MV5BOTg2NDU4Mjg2NV5BMl5BanBnXkFtZTgwNjQ0MDIyMDI@._V1_.jpg'},
        {'id': 9, 'title': ' A Minecraft Movie', 'image_url': 'https://m.media-amazon.com/images/M/MV5BYzFjMzNjOTktNDBlNy00YWZhLWExYTctZDcxNDA4OWVhOTJjXkEyXkFqcGc@._V1_.jpg'},
        {'id': 10, 'title': 'Kung Fu Panda', 'image_url': 'https://m.media-amazon.com/images/M/MV5BZDU5MDNiMGItYjVmZi00NDUxLTg2OTktNGE0NzNlNzM4NzgyXkEyXkFqcGc@._V1_.jpg'},
        # Add more...
    ]

    recommended_movies = [
        {'id': 5, 'title': 'Arrival'},
        {'id': 6, 'title': 'Ex Machina'},
        {'id': 7, 'title': 'Grand Budapest Hotel'},
        {'id': 8, 'title': 'Inception'}
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