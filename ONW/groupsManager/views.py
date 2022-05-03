from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from ONW.models import hosts,groups,network_events,backend_settings

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def add(request,ID):
    return render(request, 'add.html')

@api_view(['DELETE'])
def delete(request,ID):
    return render(request, 'remove.html')

@api_view(['PUT'])
def edit(request,ID):
    return render(request, 'edit.html')

@api_view(['GET'])
def list(request,ID):
    return render(request, 'list.html')