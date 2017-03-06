from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'base_generic.html')


def box(request, box_id):
    return render(request, 'index.html', {'box_id': box_id})
