from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('home/',views.index, name='home'),
    path('about/', views.about,),
    path('contact/', views.contact),
    path('login/', views.login, name='login'),
    path('prediction/', views.prediction),
    path('signup/', views.signup, name='signup'),
    path('error/', views.error),
]