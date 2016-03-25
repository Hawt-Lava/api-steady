from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from api.steady.models import foo
from api.steady.models import Prompt
from api.steady.models import Entry
from api.steady.models import ScoreSheet
from api.steady.provided_serializers import UserSerializer, GroupSerializer
from api.steady.serializers.foo_serializer import FooSerializer
from api.steady.serializers.entry_serializer import EntrySerializer
from api.steady.serializers.prompt_serializer import PromptSerializer
from api.steady.serializers.scoresheet_serializer import ScoreSheetSerializer


@api_view(['GET', 'POST'])
def foo_list(request):
    if request.method == 'GET':
        tasks = foo.Foo.objects.all()
        serializer = FooSerializer(tasks, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = FooSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response('Validation Failed')


@api_view(['GET', 'POST'])
def prompt(request):
    if request.method == 'GET':
        tasks = Prompt.objects.all()
        serializer = PromptSerializer(tasks, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PromptSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response('Failed')


@api_view(['GET', 'POST'])
def entry(request):
    if request.method == 'GET':
        entries = Entry.objects.all()
        serializer = EntrySerializer(entries, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = EntrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return serializer.error_messages


@api_view(['GET', 'POST'])
def scoresheet(request):
    if request.method == 'GET':
        spreadsheets = ScoreSheet.objects.all()
        serializer = ScoreSheetSerializer(spreadsheets, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ScoreSheetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response("Validation Error: {}".format(
            serializer.error_messages))


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
