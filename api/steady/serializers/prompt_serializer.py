from rest_framework import serializers
from api.steady.models.prompt import Prompt


class PromptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prompt
