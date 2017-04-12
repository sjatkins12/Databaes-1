from django.conf.urls import url

from . import views

urlpatterns = [
    # Page that displays the list of categories
    url(r'^$', views.category_list, name='category_list'),
    # Page that displays the list of subcategories pertaining to the category
    url(r'^(?P<category_name>[\w]+)/$', views.category, name='category'),
    # Page that displays the list of interest groups pertaining to the subcategory
    url(r'^[\w]+/subcategory/(?P<subcategory_name>[\w]+)/$', views.subcategory, name='subcategory'),
    # Page that displays the discussion for the given interest group
    url(r'^[\w]+/[\w]+/(?P<interest_group_name>[\w]+)/discussion$', views.DiscussionFormView.as_view(), name='box_discussion'),
    # Page that allows users to vote on a box
    url(r'^(?P<box_id>[\d]+)/vote$', views.BoxVoteFormView.as_view(), name='box_item_vote'),
]
