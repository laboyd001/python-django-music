from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Artist, Song

# Create your views here.

def index(request):
    """The home page for music history"""
    artist_list = Artist.objects.order_by('name')
    # song_list = Song.objects.order_by('-name')
    context = {
        'artist_list': artist_list,
        }
    return render(request, 'history/index.html', context)

# def detail (request, artist_id):
#     try:
#         artist = Artist.objects.get(pk=artist_id)
#     except Artist.DoesNotExist:
#         raise Http404("Artist does not exist")
#     return render(request, 'history/detail.html', {'artist': artist})

def detail(request, artist_id):
    artist = get_object_or_404(Artist, pk=artist_id)
    return render(request, 'history/detail.html', {'artist': artist})