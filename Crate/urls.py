from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from . import views

urlpatterns = [
    # Page that displays the list of categories
    url(r'^$', views.category_list, name='category_list'),
    # Page that displays the list of interest groups pertaining to the subcategory
    url(r'^category/subcategory/(?P<subcategory_name>[\w]+)/$', views.subcategory, name='subcategory'),
    # Page that displays the discussion for the given interest group
    url(r'^category/subcategory/interest_group/(?P<interest_group_name>[\w]+)/$',
        views.DiscussionFormView.as_view(), name='box_discussion'),
    # Page that allows users to vote on a box
    url(r'^(?P<box_id>[\d]+)/vote$', views.BoxVoteFormView.as_view(), name='box_item_vote'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
