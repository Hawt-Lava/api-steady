from django.db import serializers
from models.prompt import Prompt
class PromptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prompt
