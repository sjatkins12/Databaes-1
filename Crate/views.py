from django.shortcuts import render


# Create your views here.

def box_vote(request, box_id):
    return render(request, 'Crate/box_vote.html', {'box_id': box_id})


def category_list(request):
    return render(request, 'Crate/category_list.html', {})


def category(request, category_name):
    return render(request, 'Crate/category.html', {'category': category_name})


def subcategory(request, subcategory_name):
    return render(request, 'Crate/subcategory.html', {'subcategory': subcategory_name})
