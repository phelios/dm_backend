from django.db import models

from api.models.category import Category


class Project(models.Model):
    name = models.CharField(max_length=200)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
