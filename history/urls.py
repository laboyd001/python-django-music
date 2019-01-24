from django.urls import path
from . import views

app_name = 'history'
urlpatterns = [
    # Homepage
    # display all artists as links to details
    path('', views.index, name='index'),

    # localhost:8000/1/
    # display all song for artist
    path('<int:artist_id>/', views.detail, name='detail'),

    # localhost:8000/new_artist/ 
    # -- display form and POST
    path('new_artist/', views.new_artist, name='new_artist'),
    
    # localhost:8000/new_song/1
    # display song form and POST
    path('new_song/<int:artist_id>/', views.new_song, name='new_song'),
]