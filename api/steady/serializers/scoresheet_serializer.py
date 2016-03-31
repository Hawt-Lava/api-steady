from rest_framework import serializers
from api.steady.models.scoresheet import ScoreSheet
from api.steady.models.entry import Entry
from api.steady.serializers.entry_serializer import EntrySerializer


class ScoreSheetSerializer(serializers.ModelSerializer):
    entries = EntrySerializer(many=True)

    class Meta:
        model = ScoreSheet

    def create(self, validated_data):
        """Creates a scoresheet object

        Args:
            validated_data(dict): Data from scoresheet containing entries which contain prompts

        Returns:
            A scoresheet object with populated entries field
        """
        entries_data = validated_data.pop('entries')
        entry_list = []
        entry_serializer = EntrySerializer()
        for entry_data in entries_data:
            entry_list.append(entry_serializer.create(entry_data))

        score_sheet = ScoreSheet.objects.create(entries=entry_list, **validated_data)

        return score_sheet
