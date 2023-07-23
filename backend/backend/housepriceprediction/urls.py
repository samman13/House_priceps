from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('home/',views.index),
    path('about/', views.about),
    path('contact/', views.contact),
    path('login/', views.login),
    path('prediction/', views.prediction),
    path('signup/', views.signup),
    path('error/', views.error),
]