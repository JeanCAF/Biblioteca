from django.contrib import admin
from django.urls import path
from . import views

app_name = 'libro_app'

urlpatterns = [
    path('libros/', views.ListLibros.as_view(), name="libros"),
]