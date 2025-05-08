from django.shortcuts import render, redirect
from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test


@login_required
def home(request):
    popular_movies = [
    {
        'title': 'Nacho Libre',
        'image_url': 'https://m.media-amazon.com/images/M/MV5BMjMyNmEzNWYtMDNkYS00NGFmLWE3YjYtNDViYjUyMDA3MTlkXkEyXkFqcGc@._V1_.jpg',
        'imdb_url': 'https://www.imdb.com/title/tt0457510/'
    },
    {
        'title': 'School of Rock',
        'image_url': 'https://m.media-amazon.com/images/M/MV5BOTg2NDU4Mjg2NV5BMl5BanBnXkFtZTgwNjQ0MDIyMDI@._V1_.jpg',
        'imdb_url': 'https://www.imdb.com/title/tt0332379/'
    },
    {
        'title': 'A Minecraft Movie',
        'image_url': 'https://m.media-amazon.com/images/M/MV5BYzFjMzNjOTktNDBlNy00YWZhLWExYTctZDcxNDA4OWVhOTJjXkEyXkFqcGc@._V1_.jpg',
        'imdb_url': 'https://www.imdb.com/title/tt3566834/?ref_=nv_sr_srsg_0_tt_7_nm_1_in_0_q_minecra'
    },
    {
        'title': 'Kung Fu Panda',
        'image_url': 'https://m.media-amazon.com/images/M/MV5BZDU5MDNiMGItYjVmZi00NDUxLTg2OTktNGE0NzNlNzM4NzgyXkEyXkFqcGc@._V1_.jpg',
        'imdb_url': 'https://www.imdb.com/title/tt0441773/'
    },
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

@login_required
def view_reccommendations(request):
    return render(request, 'MovieManifest/view_reccommendations.html', {'title': 'view_reccommendations'})

@login_required
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


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def custom_logout(request):
    logout(request)
    return redirect('login')

from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

@user_passes_test(lambda u: u.is_superuser)
def manage_settings(request):
    users = User.objects.all().order_by('username')

    # Example settings (you'd normally pull from the DB or config)
    enable_recommendations = True
    maintenance_mode = False
    site_theme = "default"

    if request.method == 'POST':
        if 'promote_user' in request.POST:
            user_id = request.POST.get('promote_user')
            user = User.objects.filter(id=user_id).first()
            if user:
                user.is_superuser = True
                user.save()
            return redirect('manage_settings')

        if 'delete_user' in request.POST:
            user_id = request.POST.get('delete_user')
            user = User.objects.filter(id=user_id).first()
            if user and request.user.id != user.id:
                user.delete()
            return redirect('manage_settings')

        # Handle settings update
        enable_recommendations = request.POST.get('enable_recommendations') == 'True'
        maintenance_mode = request.POST.get('maintenance_mode') == 'True'
        site_theme = request.POST.get('site_theme')

        # You could store these in a model or JSON file

    return render(request, 'MovieManifest/manage_settings.html', {
        'users': users,
        'enable_recommendations': enable_recommendations,
        'maintenance_mode': maintenance_mode,
        'site_theme': site_theme
    })
