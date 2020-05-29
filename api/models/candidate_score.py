from django.db import models

from api.models.candidate import Candidate
from api.models.criterion import Criterion


class CandidateScore(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    criterion = models.ForeignKey(Criterion, on_delete=models.CASCADE)
    score = models.IntegerField()
