from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about/About.html')

def contact(request):
    return render(request,'contact/contact.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        username = authenticate(request, username=username, password=password)
        if username is not None:
            login(request, username)
            return redirect('home')
        else:
            return HttpResponse('Error, user does not exist')
    return render(request,'login/login.html', {})

def prediction(request):
    return render(request,'prediction/prediction.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password')
        password2 = request.POST.get('confirm_pass')

        new_user = User.objects.create_user(username, email, password1, password2)
        # new_user.first_name = fname
        # new_user.last_name = lname

        new_user.save()
        return redirect('login')            
          
    return render(request,'signup/signup.html', {})

def error(request):
    return render(request,'404.html')