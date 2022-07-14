from rest_framework.serializers import ModelSerializer

from api.models.criterion import Criterion


class CriterionSerializer(ModelSerializer):
    class Meta:
        model = Criterion
        fields = ['id', 'name']
