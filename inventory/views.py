from django.shortcuts import render
from rest_framework import viewsets
from .serializers import StorageSerializer

from .models import Storage


def home(request):
    storages = Storage.objects.all()
    return render(request, 'inventory/home.html', {"storages": storages})


class StorageViewSet(viewsets.ModelViewSet):
    queryset = Storage.objects.all()
    serializer_class = StorageSerializer
