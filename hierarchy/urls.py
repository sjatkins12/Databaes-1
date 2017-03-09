from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.category_list, name='list'),
    url(r'^(?P<category_name>[\w]+)/$', views.category, name='category'),
    # This must be before subcategory be otherwise it would match with subcategory
    url(r'^[\w]+/subcategory/[\w]+/interestgroup/(?P<interest_group_name>[\w]+)', views.interest_group,
        name='interest_group'),
    url(r'^[\w]+/subcategory/(?P<subcategory_name>[\w]+)', views.subcategory, name='subcategory'),
]
