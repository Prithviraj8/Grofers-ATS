from django.shortcuts import render
from .models import interview

# Create your views here.
def show_all_interview(request):
    interviews = interview.objects.all()
    print("INTERVIEWS ", interviews[0].candidate_name)
    return render(request, "interviews_log/interviews.html", {"interviews": interviews})
 # {"interviewer_name": interviews[0].interviewer_name, "candidate_name": interviews[0].candidate_name}