from django.shortcuts import render

# Create your views here.

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.decorators import api_view
# from models import Foo
from api.steady.serializers import UserSerializer, GroupSerializer


@api_view(['GET'])
def foo_list(request):
    """

    Returns:

    """
    if request.method == 'GET':
        print "Foo"




# class FooViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint test
#     """
#     # queryset = Foo.objects.all()
#     serializer_class = FooSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
