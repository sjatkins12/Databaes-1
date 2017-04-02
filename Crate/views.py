from django.shortcuts import render

from .models import Box


# Create your views here.

def crate_home(request):
    boxes = Box.objects.all()
    return render(request, 'Crate/base_crate_generic.html', context={'boxes': boxes})


def box(request, box_id):
    return render(request, 'Crate/crate_index.html', {'box_id': box_id})


def previous(request):
    return render(request, 'Crate/previous.html', {})


def item_home(request):
    return render(request, 'Crate/item_index.html', {})


def item(request, item_id):
    return render(request, 'Crate/item.html', {'item_id': item_id})
