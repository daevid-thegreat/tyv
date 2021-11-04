from django.shortcuts import render , redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse 
from .models import Profile


# Create your views here.
@login_required(login_url='guest')
def home(request):
    return render(request, 'home.html')

def guest(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Sorry we cannot find this user')
            return redirect('guest')
    return render(request, 'homefornewuser.html')

def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name =  request.POST['last_name']
        username =  request.POST['username'] 
        email =  request.POST['email']
        password =  request.POST['password']

        if User.objects.filter(email=email).exists():
            messages.info(request, "This email has already been used")
            return redirect('signup')
        elif User.objects.filter(username=username).exists():
            messages.info(request, "This username has been taken")
        else:
            user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
            user.save()

            user_model = User.objects.get(username=username)
            new_profile = Profile.objects.create(user=user_model, id_user = user_model.id)
            new_profile.save( )
            return redirect('guest')
    return render(request, 'signup.html')

@login_required(login_url='guest')
def logout(request):
        auth.logout(request)
        return redirect('guest')

@login_required(login_url='guest')
def settings(request):
    return render(request, 'settings.html')