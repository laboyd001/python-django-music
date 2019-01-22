from django.shortcuts import render
from .models import Artist
from .models import Song

# Create your views here.

def index(request):
    """The home page for music history"""
    artist_list = Artist.objects.order_by('-name')
    song_list = Song.objects.order_by('-name')
    context = {
        'artist_list': artist_list,
        'song_list': song_list,
        }
    return render(request, 'history/index.html', context)
