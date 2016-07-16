from api.steady.models.scoresheet import ScoreSheet
from api.steady.serializers.scoresheet_serializer import ScoreSheetSerializer
from rest_framework import filters
from rest_framework import generics


class ScoreSheetView(generics.ListCreateAPIView):
    """
    ScoreSheet View for Listing and Creating
    """
    serializer_class = ScoreSheetSerializer
    filter_backends = (filters.DjangoFilterBackend, )

    def get_queryset(self):
        queryset = ScoreSheet.objects.all()
        device_id = self.request.query_params.get('device_id', None)

        if device_id is not None:
            queryset = queryset.filter(device_id=device_id)
        return queryset
