from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError


def signupuser(request):
    if request.method == 'GET':
        return render(request, 'user/signup.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    request.POST['username'],
                    password=request.POST['password1']
                )
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'user/signup.html',
                              {'form': UserCreationForm(), 'error': 'User with this name already exists'})
        else:
            return render(request, 'user/signup.html',
                          {'form': UserCreationForm(), 'error': 'Passwords are not the same'})


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'user/loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'user/loginuser.html',
                          {'form': AuthenticationForm(), 'error': 'Invalid login information'})
        else:
            login(request, user)
            return redirect('home')


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
