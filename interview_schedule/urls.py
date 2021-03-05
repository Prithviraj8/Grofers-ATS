from django.contrib import admin
from django.urls import path, include
from . import schedule_views

app_name = "interview_schedule"

urlpatterns = [
    path('', schedule_views.schedule_interviews, name='Schedule'),
]
