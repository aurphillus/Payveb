from django.contrib import admin
from django.urls import path, include
from . import views

app_name="dashboard"

urlpatterns = [
    path('add_dealer/', views.add_dealer, name="add_dealer" ),

]
