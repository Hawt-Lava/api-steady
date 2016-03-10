from rest_framework import serializers
from api.steady.models.scoresheet import ScoreSheet


class ScoreSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScoreSheet
