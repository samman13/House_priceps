from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about/About.html')

def contact(request):
    return render(request,'contact/contact.html')

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')  # Redirect to user's profile page
    else:
        form = AuthenticationForm()
    return render(request,'login/login.html', {'form': form})

def prediction(request):
    return render(request,'prediction/prediction.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/page/login')  # Redirect to user's profile page
    else:
        form = UserCreationForm()
            
            
    return render(request,'signup/signup.html', {'form':form})

def error(request):
    return render(request,'404.html')