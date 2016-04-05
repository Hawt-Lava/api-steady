from api.steady.models.scoresheet import ScoreSheet
from api.steady.serializers.scoresheet_serializer import ScoreSheetSerializer
from rest_framework import filters
from rest_framework import generics


class ScoreSheetView(generics.ListCreateAPIView):
    """
    ScoreSheet View for Listing and Creating
    """
    queryset = ScoreSheet.objects.all()
    serializer_class = ScoreSheetSerializer
    filter_backends = (filters.DjangoFilterBackend, )
