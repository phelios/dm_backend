from api.models.candidate_score import CandidateScore
from api.serializers.candidate_score_serializer import CandidateScoreSerializer
from rest_framework import generics


class CandidateScoreList(generics.ListCreateAPIView):
    queryset = CandidateScore.objects.all()
    serializer_class = CandidateScoreSerializer

    def get_queryset(self):
        queryset = CandidateScore.objects.all()
        candidate_id = self.request.query_params.get('candidate_id')
        if candidate_id is not None:
            queryset = queryset.filter(candidate_id=candidate_id)
        return queryset


class CandidateScoreDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CandidateScore.objects.all()
    serializer_class = CandidateScoreSerializer
