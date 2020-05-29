from api.models.project_criteria import ProjectCriteria
from api.serializers.project_criteria_serializer import ProjectCriteriaSerializer
from rest_framework import generics


class ProjectCriteriaList(generics.ListCreateAPIView):
    queryset = ProjectCriteria.objects.all()
    serializer_class = ProjectCriteriaSerializer


class ProjectCriteriaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProjectCriteria.objects.all()
    serializer_class = ProjectCriteriaSerializer
