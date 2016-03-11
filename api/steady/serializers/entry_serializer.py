from rest_framework import serializers
from api.steady.models.entry import Entry


class EntrySerializer(serializers.ModelSerializer):
    prompt = serializers.StringRelatedField()

    class Meta:
        model = Entry
