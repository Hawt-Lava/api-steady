from api.steady.tests.base_test import BaseTest
from api.steady.views.prompt_view import PromptView

from rest_framework.test import APIRequestFactory
class PromptViewTest(BaseTest):
    def test_successful_request(self):
        factory = APIRequestFactory()
        request = factory.get('prompts')
        view = PromptView()
        response = view.get(request)
        self.assertFalse(response)
