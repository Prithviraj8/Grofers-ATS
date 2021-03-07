from django.shortcuts import render
from Calendar import list_events, create_event
from interview_schedule.models import interviewer
from .forms import CreateEventForm
from django import forms


def schedule_interviews(request):
    interviewers = interviewer.objects.all()
    return render(request, "schedule/schedule.html", {"interviewers": interviewers})


def view_calendar(request):
    print(" REQ ", request.POST)
    if request.POST.get("id"):
        print(request.POST.get("id"))
    interviewers = interviewer.objects.all()
    email = interviewers[0].email
    events = list_events.get_events(str(email))
    return render(request, 'calendarEvents/calendarEvents.html', {'interviewers': interviewers, 'events': events})


def create_event_(request):
    form = CreateEventForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            print("in is valid")
            create_event.create_event()
        print("request data ", request.POST)
        print("form ", form)
    return render(request, 'calendarEvents/calendarEvents.html', {'form': form})

