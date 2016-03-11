from rest_framework import serializers
from api.steady.models.entry import Entry
from api.steady.models.prompt import Prompt


class EntrySerializer(serializers.ModelSerializer):
    prompt = serializers.StringRelatedField()

    class Meta:
        model = Entry

    def create(self, validated_data):

        prompt_data = validated_data.get('prompt')

        entry = Entry.objects.create(**validated_data)
        prompt = Prompt.objects.create(**prompt_data)
        entry.prompt = prompt.pk

        return entry

