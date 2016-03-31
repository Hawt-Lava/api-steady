from rest_framework import serializers
from api.steady.models.entry import Entry
from api.steady.models.prompt import Prompt
from api.steady.serializers.prompt_serializer import PromptSerializer


class EntrySerializer(serializers.ModelSerializer):
    prompt = PromptSerializer()

    class Meta:
        model = Entry

    def create(self, validated_data):
        """Takes the prompt data and displays it in the entry field

        Args:
            validated_data(str): Data from entry and prompt

        Returns:
            An entry model with a populated prompt
        """

        prompt_data = validated_data.pop('prompt')
        prompt = Prompt.objects.create(**prompt_data)
        entry = Entry.objects.create(prompt=prompt, **validated_data)

        entry.prompt = prompt

        return entry
