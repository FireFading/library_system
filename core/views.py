from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required

from .models import User


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password != password2:
            messages.info(request, 'Password mismatch')
            return redirect('signup')

        if User.objects.filter(email=email).exists():
            messages.info(request, 'Email already exists')
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.info(request, 'Username already exists')
            return redirect('signup')
        
        new_user = User.objects.create(username=username, email=email, password=password)
        new_user.save()
        
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        
        messages.info(request, 'Something wrong with registration')
        
    return render(request, 'auth/signup.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Login successful')
            return redirect('home')
        
        messages.error(request, 'User not found')
    return render(request, 'auth/signin.html')


@login_required(login_url='signin')
def logout(request):
    auth.logout(request)
    return redirect('signin')
