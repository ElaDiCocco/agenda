#from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.contacto_index, name='index', )
]