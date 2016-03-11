from rest_framework import serializers
from api.steady.models.scoresheet import ScoreSheet
from api.steady.models.entry import Entry
from api.steady.serializers.entry_serializer import EntrySerializer


class ScoreSheetSerializer(serializers.ModelSerializer):
    entries = EntrySerializer(many=True)

    class Meta:
        model = ScoreSheet

    def create(self, validated_data):
        entries_data = validated_data.pop('entries')
        score_sheet = ScoreSheet.objects.create(**validated_data)
        entry_list = []
        for entry_data in entries_data:
            entry_list.append(Entry.objects.create(**entry_data))
        score_sheet.entries = entry_list
        return score_sheet
