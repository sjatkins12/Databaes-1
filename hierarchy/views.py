from django.shortcuts import render


# Create your views here.
def category(request, category_name):
    return render(request, 'hierarchy/category.html', {'category': category_name})


def subcategory(request, subcategory_name):
    return render(request, 'hierarchy/subcategory.html', {'subcategory': subcategory_name})


def interest_group(request, interest_group_name):
    return render(request, 'hierarchy/interest_group.html', {'interest_group': interest_group_name})
