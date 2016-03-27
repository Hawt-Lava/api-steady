from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions


class PromptViewTest(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
