from datetime import date

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View

from .forms import ReportForm, DiscussionForm
from .models import Category, SubCategory, InterestGroup, SellingCycle, Box, Item


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
    category_subcategory_map = {}
    for category in Category.objects.order_by('pk'):
        changed = False
        for sub_category in SubCategory.objects.filter(category_name__category_name__icontains=category.category_name):
            if category_subcategory_map.get(category) is None:
                category_subcategory_map[category] = [sub_category]
            else:
                category_subcategory_map.get(category).append(sub_category)
            changed = True
        # Could just be done by checking len -- This just makes sure sub_category table is populated
        if not changed:
            category_subcategory_map[category] = []
    if len(category_subcategory_map) == 0:
        category_width = 0
    else:
        category_width = 100 / len(category_subcategory_map)
    return render(request, 'Crate/category_list.html',
                  {'category_map': category_subcategory_map,
                   'category_width': category_width})


def subcategory(request, category_name, subcategory_name):
    # TODO: Merge Voting into this page and display it towards the bottom (redirect to homepage after vote)
    interest_groups = InterestGroup.objects.filter(subcategory_name__subcategory_name__icontains=subcategory_name)
    curr_selling_cycle = SellingCycle.objects.filter(cycle_date__lte=date.today()).order_by('-cycle_date').first()
    curr_boxes_sold = Box.objects.filter(sold_during=curr_selling_cycle)
    interest_group_items = {}
    for interest_group in interest_groups:
        interest_group_box = curr_boxes_sold.filter(type=interest_group)
        for item in Item.objects.filter(contained_in=interest_group_box):
            if interest_group_items.get(interest_group) is None:
                interest_group_items[interest_group] = [item]
            else:
                interest_group_items[interest_group].append(item)
    return render(request, 'Crate/subcategory.html',
                  {'category': category_name,
                   'subcategory': subcategory_name,
                   'interest_group': interest_group_items,
                   'interest_width': 100 / len(interest_group_items)})
