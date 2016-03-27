from api.steady.serializers.prompt_serializer import PromprtSerializer
from api.steady.views.base_view import BaseView


class PromptView(BaseView):

    serializer_class = PromprtSerializer
