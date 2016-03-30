from api.steady.models.prompt import Prompt
from api.steady.serializers.prompt_serializer import PromptSerializer

from rest_framework import generics


class PromptView(generics.ListCreateAPIView):
    """
    Prompt View for Creating or Fetching all prompts
    """

    queryset = Prompt.objects.all()
    serializer_class = PromptSerializer
