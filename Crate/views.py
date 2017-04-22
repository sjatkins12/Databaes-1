from datetime import date

from django.http import HttpResponseRedirect
from django.shortcuts import render, get_list_or_404
from django.views.generic import View

from user_profile.models import UserProfile
from .forms import ReportForm, DiscussionForm
from .models import Category, SubCategory, InterestGroup, SellingCycle, Box, Item, Discussion


# Create your views here.

class BoxVoteFormView(View):
    def get(self, request, *args, **kwargs):
        form = ReportForm()
        curr_selling_cycle = SellingCycle.objects.filter(cycle_date__lte=date.today()).order_by('-cycle_date').first()
        box_vote = Box.objects.filter(sold_during=curr_selling_cycle, id=kwargs['box_id'])
        items = []
        for item in Item.objects.filter(contained_in=box_vote):
            items.append(item)
        if len(items) == 0:
            box_width = 0
        else:
            box_width = 100 / len(items)
        return render(request, 'Crate/box_vote.html',
                      {'box_id': kwargs['box_id'],
                       'items': items,
                       'box_width': box_width,
                       'form': form})

    def post(self, request, *args, **kwargs):
        form = ReportForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('')


class DiscussionFormView(View):
    form_class = DiscussionForm

    def get(self, request, *args, **kwargs):
        form = DiscussionForm()
        interest_group_name = kwargs['interest_group_name']
        interest_group = InterestGroup.objects.get(interest_group_name=interest_group_name)
        discussions = Discussion.objects.filter(interest=interest_group).order_by('-pk')[:10]
        return render(request, 'Crate/box_discussion.html',
                      {'category_name': kwargs['category_name'],
                       'subcategory_name': kwargs['subcategory_name'],
                       'interest_group_name': interest_group_name,
                       'cost': interest_group.subscription_cost,
                       'discussions': discussions,
                       'form': form})

    def post(self, request, *args, **kwargs):
        form = DiscussionForm(request.POST)
        if form.is_valid():
            comment = form.cleaned_data.get('comment')
            user = UserProfile.objects.get(user=request.user)
            interest_group = InterestGroup.objects.get(interest_group_name=kwargs['interest_group_name'])
            Discussion.objects.create(comment=comment, user=user, interest=interest_group)
            return HttpResponseRedirect('')
        else:
            return HttpResponseRedirect('')


def category_list(request):
    category_subcategory_map = {}
    for category in get_list_or_404(Category):
        changed = False
        for sub_category in SubCategory.objects.filter(category__category_name=category.category_name):
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


def subcategory_list(request, category_name):
    subcategory_interest_map = {}
    for subcategory in get_list_or_404(SubCategory, category__category_name=category_name):
        changed = False
        for interest_group in InterestGroup.objects.filter(subcategory=subcategory):
            if subcategory_interest_map.get(subcategory) is None:
                subcategory_interest_map[subcategory] = [interest_group]
            else:
                subcategory_interest_map[subcategory].append(interest_group)
            changed = True
        if not changed:
            subcategory_interest_map[subcategory] = []
    if len(subcategory_interest_map) == 0:
        subcategory_width = 0
    else:
        subcategory_width = 100 / len(subcategory_interest_map)
    return render(request, 'Crate/subcategory_list.html',
                  {'category_name': category_name,
                   'subcategory': subcategory_interest_map,
                   'subcategory_width': subcategory_width})


def interest_group_list(request, category_name, subcategory_name):
    interest_groups = get_list_or_404(InterestGroup, subcategory__subcategory_name=subcategory_name)
    if len(interest_groups) == 0:
        interest_width = 0
    else:
        interest_width = 100 / len(interest_groups)
    return render(request, 'Crate/interest_group_list.html',
                  {'category_name': category_name,
                   'subcategory_name': subcategory_name,
                   'interest_groups': interest_groups,
                   'interest_width': interest_width})
