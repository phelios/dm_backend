from rest_framework.serializers import ModelSerializer

from api.models.candidate import Candidate


class CandidateSerializer(ModelSerializer):
    class Meta:
        model = Candidate
        fields = ['id', 'project_id', 'name', 'description']
