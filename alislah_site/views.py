from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, 'index.html')


def gallery(request):
    return render(request, "gallery.html")


def admission(request):
    return render(request, "admission.html")


def academics(request):
    return render(request, "academics.html")


def contacts(request):
    return render(request, "contacts.html")
