from django.shortcuts import render
from Sangeet.models import Song
# Create your views here.
def index(request):
    song = Song.objects.all()
    return render(request, 'index.htm', {'song' :song})

def songs(request):
    song = Song.objects.all()
    return render(request, 'Sangeet/songs.htm', {'song' :song})

def songpost(request,id):
    song = Song.objects.filter(id=id).first()
    return render(request, 'Sangeet/songpost.htm', {'song' :song})
