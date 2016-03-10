
from api.steady.models.foo import Foo

from rest_framework import serializers


class FooSerializer(serializers.ModelSerializer):
    class Meta:
        model = Foo
