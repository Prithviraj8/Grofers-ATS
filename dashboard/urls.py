from django.contrib import admin
from django.urls import path, include
from . import dashboard_views

app_name = "dashboard"

urlpatterns = [
    path('', dashboard_views.dashboard, name='Dashboard'),
    path('schedule/', include("interview_schedule.urls")),
]
