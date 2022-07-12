from django.shortcuts import render
from .models import Storage


def home(request):
    storages = Storage.objects.all()
    return render(request, 'inventory/home.html', {"storages": storages})
