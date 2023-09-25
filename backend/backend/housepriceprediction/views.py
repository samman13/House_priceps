from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserRegisterForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about/About.html')

def contact(request):
    return render(request,'contact/contact.html')

def login(request):
    return render(request,'login/login.html')

def prediction(request):
    return render(request,'prediction/prediction.html')

def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username =form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, your account has created sucessfully')
            return redirect('/page/login')
        else:
            form = UserRegisterForm()
            
            
    return render(request,'signup/signup.html', {'form':form})

def error(request):
    return render(request,'404.html')