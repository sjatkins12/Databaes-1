from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View

from .forms import ReportForm, DiscussionForm
from .models import Category, SubCategory, InterestGroup


# Create your views here.

class BoxVoteFormView(View):
    def get(self, request, *args, **kwargs):
        form = ReportForm()
        return render(request, 'Crate/box_vote.html', {'box_id': kwargs['box_id'], 'form': form})

    def post(self, request, *args, **kwargs):
        form = ReportForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('')


class DiscussionFormView(View):
    def get(self, request, *args, **kwargs):
        form = DiscussionForm()
        return render(request, 'Crate/box_discussion.html',
                      {'interest_group': kwargs['interest_group_name'], 'form': form})

    def post(self, request, *args, **kwargs):
        form = DiscussionForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('')


def category_list(request):
    cat_subcat_map = {}
    for category in Category.objects.order_by('pk'):
        for sub_category in SubCategory.objects.filter(category_name__category_name__icontains=category.category_name):
            if cat_subcat_map.get(category) is None:
                cat_subcat_map[category] = [sub_category]
            else:
                cat_subcat_map.get(category).append(sub_category)
            continue
        cat_subcat_map[category] = []
    if len(cat_subcat_map) == 0:
        category_width = 0
    else:
        category_width = 100 / len(cat_subcat_map)
    return render(request, 'Crate/category_list.html',
                  {'category_map': cat_subcat_map,
                   'category_width': category_width})


def subcategory(request, subcategory_name):
    interest_groups = InterestGroup.objects.filter(subcategory_name__subcategory_name__icontains=subcategory_name)
    return render(request, 'Crate/subcategory.html',
                  {'subcategory': subcategory_name,
                   'interest_group': interest_groups,
                   'interest_width': 100 / len(interest_groups)})
