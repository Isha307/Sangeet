from email import message
from django.shortcuts import redirect, render
from Sangeet.models import Song, Watchlater
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.shortcuts import redirect

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

def logout(request):
    return render(request, 'Sangeet/logout.htm')

def watchlater(request):
    if request.method=="POST":
        user = request.user
        video_id = request.POST['video_id']
        message = "Your Video is Successfully Added"
        watch = Watchlater.objects.filter(user = user)
        for i in watch:
            if video_id  == i.video_id:
                message = "Your Video is already Present"
                break
            else:
                watchlater = Watchlater(user=user, video_id = video_id)
                watchlater.save()
                message = "Your Video is Successfully Added"
        song = Song.objects.filter(id=video_id).first()
        return redirect(f"songs/{video_id}", {"song":song ,"message" : message})
    return render(request, 'Sangeet/watchlater.htm')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        pass3 = request.POST['pass3']
        user = authenticate(username=username, password = pass3)
        from django.contrib.auth import login
        login(request,user)
        return redirect('/')
    return render(request, 'Sangeet/login.htm')

def signup(request):
    if request.method == "POST":
        email = request.POST['email']
        username = request.POST['username']
        pass1 = request.POST['pass1']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        pass2 = request.POST['pass2']

        myuser = User.objects.create_user(email, username, pass1)
        myuser.first_name = first_name
        myuser.last_name = last_name
        myuser.save()
        user = authenticate(username=username, password = pass1)
        from django.contrib.auth import login
        login(request,user)
        return redirect('/')

    return render(request, 'Sangeet/signup.htm')