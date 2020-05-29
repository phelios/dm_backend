from api.models.criterion import Criterion
from api.serializers.criterion_serializer import CriterionSerializer
from rest_framework import generics


class CriterionList(generics.ListCreateAPIView):
    queryset = Criterion.objects.all()
    serializer_class = CriterionSerializer


class CriterionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Criterion.objects.all()
    serializer_class = CriterionSerializer
