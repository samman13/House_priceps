from django.shortcuts import render
from django.http import HttpResponse
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
    return render(request,'signup/signup.html')

def error(request):
    return render(request,'404.html')