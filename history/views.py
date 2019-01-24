from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Artist, Song
# from .forms import ArtistForm, SongForm

# Create your views here.

def index(request):
    """The home page for music history"""
    artist_list = Artist.objects.order_by('name')
    context = {
        'artist_list': artist_list,
        }
    return render(request, 'history/index.html', context)

def detail(request, artist_id):
    """the artist detail page"""
    artist = get_object_or_404(Artist, pk=artist_id)
    return render(request, 'history/detail.html', {'artist': artist})

# def new_artist(request):
#     """Add a new artist"""
#     if request.method != 'POST':
#         # No data submitted; create a blank form.
#         form = ArtistForm()
#     else:
#         # POST data submitted; process data.
#         form = ArtistForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('history:index'))
        
#     context = {'form': form}
#     return render(request, 'history/new_artist.html', context)


# def new_artist_form(request):
#     """new artist form"""
#     return render(request, 'history/new_artist.html')


def new_artist(request):
    """Add new artist"""
    if request.method != 'POST':   
        return render(request, 'history/new_artist.html')
    else:
        artist = request.POST['artist_name']
        a = Artist(name = artist)
        a.save()
        return HttpResponseRedirect(reverse('history:index'))



# def new_song(request, artist_id):
#     """Add a new song for a particular artist"""
#     artist = Artist.objects.get(id=artist_id)

#     if request.method != 'POST':
#         # No data submitted; create a blank form.
#         form = SongForm()
#     else:
#         # POST data submitted; process data.
#         form = SongForm(data=request.POST)
#         if form.is_valid():
#             # next 3 lines makes sure that you save the song 
#             # with the right artist id
#             new_song = form.save(commit=False)
#             new_song.artist = artist
#             new_song.save()
#             return HttpResponseRedirect(reverse('history:detail', args=[artist_id]))
    
#     context = {'artist': artist, 'form': form}
#     return render(request, 'history/new_song.html', context)
