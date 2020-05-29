from django.db import models

from api.models.project import Project
from api.models.criterion import Criterion


class ProjectCriteria(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    criterion = models.ForeignKey(Criterion, on_delete=models.CASCADE)
