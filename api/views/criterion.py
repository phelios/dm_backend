from api.models.criterion import Criterion
from api.serializers.criterion_serializer import CriterionSerializer
from rest_framework import generics


class CriterionList(generics.ListCreateAPIView):
    queryset = Criterion.objects.all().order_by('pk')
    serializer_class = CriterionSerializer

    def get_queryset(self):
        queryset = Criterion.objects.all()
        project_id = self.request.query_params.get('project_id')
        if project_id is not None:
            queryset = queryset.filter(projectcriteria__project_id=project_id)
        return queryset


class CriterionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Criterion.objects.all()
    serializer_class = CriterionSerializer
