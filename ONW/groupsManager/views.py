from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from ONW.models import hosts,groups,network_events,backend_settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from functions.serializers import *
from functions.data_validations import *

@api_view(['POST'])
def add(request):
    if request.method == 'POST':
        app_id = request.POST.get('app_id')
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        group = groups(name=name,desc=desc,app_id=app_id)
        group.save()
        return Response(messagesHandler('ONW200'))

@api_view(['DELETE'])
def delete(request,ID):
    if request.method == 'DELETE':
        group = get_object_or_404(groups,id=ID)
        group.delete()
        return Response(messagesHandler('ONW202'))

@api_view(['PUT'])
def edit(request,ID):
    if request.method == 'PUT':
        group = get_object_or_404(groups,id=ID)
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        group.name = name
        group.desc = desc
        group.save()
        return Response(messagesHandler('ONW201'))

@api_view(['GET'])
def view(request,ID):
    if request.method == 'GET':
        group = get_object_or_404(groups,id=ID)
        serializer = groupsSerializer(group)
        return Response(serializer.data)

@api_view(['GET'])
def list(request):
    if request.method == "GET":
        groups_list = groups.objects.all()
        serializer = groupsSerializer(groups_list, many=True)
    return  Response(serializer.data)
