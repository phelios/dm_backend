from django.db import models


class Criterion(models.Model):
    name = models.CharField(max_length=200)
    weight = models.IntegerField()


class CriteriaSet(models.Model):
    name = models.CharField(max_length=200)
    criterion = models.ForeignKey(Criterion, on_delete=models.CASCADE)


class Candidate(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()


class Project(models.Model):
    name = models.CharField(max_length=200)
    candidates = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    criteria_set = models.ForeignKey(CriteriaSet, on_delete=models.CASCADE)


class CandidateScore(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    criterion = models.ForeignKey(Criterion, on_delete=models.CASCADE)
    score = models.IntegerField()
