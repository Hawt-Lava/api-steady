from rest_framework import serializers
from api.steady.models.scoresheet import ScoreSheet
from api.steady.models.entry import Entry


class ScoreSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScoreSheet

    def create(self, validated_data):
        entries_data = validated_data.pop('entries')
        scoreSheet = ScoreSheet.objects.create(**validated_data)
        for entry_data in entries_data:
            Entry.objects.create(**entry_data)
        return scoreSheet
