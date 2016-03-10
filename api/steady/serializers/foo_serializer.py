
from rest_framework import serializers
from api.steady.models.foo import Foo


class FooSerializer(serializers.ModelSerializer):
    class Meta:
        model = Foo
