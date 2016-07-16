from api.steady.models.user import User
from api.steady.serializers.user_serializer import UserSerializer

from rest_framework import generics


class UserView(generics.ListCreateAPIView):
    """
    User View for Creating or Fetching all prompts
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
