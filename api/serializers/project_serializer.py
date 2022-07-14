from rest_framework.serializers import ModelSerializer

from api.models.project import Project


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', "category_id"]
