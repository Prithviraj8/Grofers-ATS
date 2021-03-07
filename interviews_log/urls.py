from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "interviews_log"

urlpatterns = [
    path('', views.show_all_interview, name='ShowInterviews'),
]
