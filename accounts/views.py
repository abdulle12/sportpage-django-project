from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages

# Create your views here.

def login(request):
    errors = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            return redirect('/')
        else:
            errors['invalid'] = 'Invalid username or password'
    
    return render(request, 'login.html', {'errors': errors})

def register(request):
    errors = {}
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        
        if password1 != password2:
            errors['password'] = 'Passwords do not match'
        else:
            if User.objects.filter(username=username).exists():
                errors['username'] = 'Username is taken'
            elif User.objects.filter(email=email).exists():
                errors['email'] = 'Email is taken'
            else:
                user = User.objects.create_user(username=username, password=password1, email=email,
                                                first_name=first_name, last_name=last_name)
                user.save()
                return redirect('login')
    
    return render(request, 'register.html', {'errors': errors})
    
def logout(request):
    auth_logout(request)
    return redirect('/')
