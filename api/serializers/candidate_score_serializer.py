from rest_framework.serializers import ModelSerializer

from api.models.candidate_score import CandidateScore


class CandidateScoreSerializer(ModelSerializer):
    class Meta:
        model = CandidateScore
        fields = ['id', 'candidate_id', 'criterion_id', 'score']
