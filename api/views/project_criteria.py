from api.models.project_criteria import ProjectCriteria
from api.serializers.project_criteria_serializer import ProjectCriteriaSerializer
from rest_framework import generics


class ProjectCriteriaList(generics.ListCreateAPIView):
    queryset = ProjectCriteria.objects.all()
    serializer_class = ProjectCriteriaSerializer

    def get_queryset(self):
        queryset = ProjectCriteria.objects.all()
        project_id = self.request.query_params.get('project_id')
        if project_id is not None:
            queryset = queryset.filter(project_id=project_id)
        return queryset


class ProjectCriteriaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProjectCriteria.objects.all()
    serializer_class = ProjectCriteriaSerializer
