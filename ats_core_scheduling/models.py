from django.db import models
from home_app.models import Recruiter


# Create your models here.
class interviewer_candidate(models.Model):
    interviewer_id = models.ForeignKey(Recruiter, on_delete=models.CASCADE)
    # candidate_id = models.ForeignKey()
    interview_stage = models.CharField(max_length=50)
    interview_schedule_time = models.CharField()
    interviewer_feedback = models.CharField()

    def __str__(self):
        return self.interviewer_id.id
