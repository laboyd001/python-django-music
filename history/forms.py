from django import forms
from .models import Artist, Song

class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['name']
        labels = {'name': ''}


class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['name']
        labels = {'name': ''}