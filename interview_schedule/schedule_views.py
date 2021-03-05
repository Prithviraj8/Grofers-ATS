from django.shortcuts import render


# Create your views here.
def schedule_interviews(request):
    return render(request, "schedule/schedule.html")
