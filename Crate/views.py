from django.shortcuts import render

from .models import Box


# Create your views here.

def index(request):
    boxes = Box.objects.all()
    return render(request, 'base_generic.html', context={'boxes': boxes})


def box(request, box_id):
    return render(request, 'index.html', {'box_id': box_id})


def previous(request):
    return render(request, 'previous.html', {})
