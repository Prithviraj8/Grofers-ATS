from django.shortcuts import render, redirect
from Calendar import list_events, create_event
from .models import interviewer
from interviews_log.models import interview
from .forms import CreateEventForm
from .validate_time_date import validate
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
    print("CREATING EVENT ")
    form = CreateEventForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            print(" REQUEST ", request.POST)
            time_start = request.POST['time_start']
            time_end = request.POST['time_start']
            validated_time = validate(time_start, time_end)
            create_event.create_event(validated_time)

        interviews = interview.objects.all()
        return render(request, 'interviews_log/interviews.html', {"interviews": interviews})
    return render(request, 'calendarEvents/calendarEvents.html', {'form': form})

