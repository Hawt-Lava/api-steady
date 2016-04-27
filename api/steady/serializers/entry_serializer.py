from rest_framework import serializers
from api.steady.models.entry import Entry
from api.steady.models.prompt import Prompt
from api.steady.serializers.prompt_serializer import PromptSerializer


class EntrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Entry

