
from django.db import serializers
from models.foo import Foo
class FooSerializer(serializers.ModelSerializer)
    class Meta:
        model = Foo
