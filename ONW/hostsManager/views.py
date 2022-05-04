from tokenize import group
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
        hostname = request.POST.get('hostname')
        ip = request.POST.get('ip')
        desc = request.POST.get('desc')
        group = get_object_or_404(groups,id=request.POST.get('group'))
        host = hosts(hostname=hostname,ip=ip,desc=desc,group=group)
        host.save()
        return Response(messagesHandler('ONW200'))

@api_view(['DELETE'])
def delete(request,ID):
    if request.method == 'DELETE':
        host = get_object_or_404(hosts,id=ID)
        host.delete()
        return Response(messagesHandler('ONW202'))


@api_view(['PUT'])
def edit(request,ID):
    if request.method == 'PUT':
        host = get_object_or_404(hosts,id=ID)
        hostname = request.POST.get('hostname')
        group = get_object_or_404(groups,id=request.POST.get('group'))
        ip = request.POST.get('ip')
        desc = request.POST.get('desc')
        host.hostname = hostname
        host.ip = ip
        host.desc = desc
        host.group = group
        host.save()
        return Response(messagesHandler('ONW201'))


@api_view(['GET'])
def view(request,ID):
    if request.method == 'GET':
        host = get_object_or_404(hosts,id=ID)
        serializer = hostsSerializer(host)
        return Response(serializer.data )

@api_view(['GET'])
def list(request):
    if request.method == "GET":
        hosts_list = hosts.objects.all()
        serializer = hostsSerializer(hosts_list, many=True)
    return  Response(serializer.data)
