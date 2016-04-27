from rest_framework import serializers
from api.steady.models.user import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
