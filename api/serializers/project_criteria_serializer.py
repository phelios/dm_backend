from rest_framework.serializers import ModelSerializer

from api.models.project_criteria import ProjectCriteria


class ProjectCriteriaSerializer(ModelSerializer):
    class Meta:
        model = ProjectCriteria
        fields = ['id', 'project', 'criterion', 'weight']
