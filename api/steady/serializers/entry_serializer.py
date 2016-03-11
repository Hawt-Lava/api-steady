from rest_framework import serializers
from api.steady.models.entry import Entry
from api.steady.models.prompt import Prompt
from api.steady.serializers.prompt_serializer import PromptSerializer


class EntrySerializer(serializers.ModelSerializer):
    prompt = PromptSerializer()

    class Meta:
        model = Entry

    def create(self, validated_data):

        prompt_data = validated_data.pop('prompt')

        entry = Entry.objects.create(**validated_data)
        prompt = Prompt.objects.create(**prompt_data)
        entry.prompt = prompt

        return entry
