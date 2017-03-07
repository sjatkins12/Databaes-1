from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'item/index.html', {})


def item(request, item_id):
    return render(request, 'item/item.html', {'item_id': item_id})
