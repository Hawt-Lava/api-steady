from rest_framework import serializers
from api.steady.models.entry import Entry


class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
