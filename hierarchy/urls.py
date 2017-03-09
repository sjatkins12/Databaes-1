from django.conf.urls import url

from . import views

urlpatterns = [
    # This must be first be otherwise it would match with subcategory
    url(r'^[\w]+/subcategory/[\w]+/interestgroup/(?P<interest_group_name>[\w]+)', views.interest_group,
        name='interest_group'),
    url(r'^(?P<category_name>[\w]+)/$', views.category, name='category'),
    url(r'^[\w]+/subcategory/(?P<subcategory_name>[\w]+)', views.subcategory, name='subcategory'),
]
