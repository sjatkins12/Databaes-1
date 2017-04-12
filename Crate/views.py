from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View

from .forms import ReportForm, DiscussionForm


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
        return render(request, 'Crate/box_discussion.html', {'interest_group': kwargs['interest_group_name'], 'form': form})

    def post(self, request, *args, **kwargs):
        form = DiscussionForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('')


def category_list(request):
    return render(request, 'Crate/category_list.html', {})


def category(request, category_name):
    return render(request, 'Crate/category.html', {'category': category_name})


def subcategory(request, subcategory_name):
    return render(request, 'Crate/subcategory.html', {'subcategory': subcategory_name})
