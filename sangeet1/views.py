from django.shortcuts import render
from Sangeet.models import Song
# Create your views here.
def index(request):
    song = Song.objects.all()
    return render(request, 'index.htm', {'song' :song})