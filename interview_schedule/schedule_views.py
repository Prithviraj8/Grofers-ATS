from django.shortcuts import render
from Calendar import list_events
from interview_schedule.models import interviewer


def schedule_interviews(request):
    return render(request, "schedule/schedule.html")


def view_calendar(request):
    interviewers = interviewer.objects.all()
    email = interviewers[0].email
    events = list_events.get_events(str(email))
    return render(request, 'calendarEvents/calendarEvents.html', {'interviewers': interviewers, 'events': events})
