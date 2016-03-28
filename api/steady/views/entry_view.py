from api.steady.models.entry import Entry
from api.steady.serializers.entry_serializer import EntrySerializer

from rest_framework import generics


class EntryView(generics.ListCreateAPIView):
    """
    Entry View for Listing and Creating
    """

    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
