from django.db import models

from api.models.project import Project
from api.models.criterion import Criterion


class ProjectCriteria(models.Model):
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    criterion_id = models.ForeignKey(Criterion, on_delete=models.CASCADE)
    weight = models.IntegerField()
