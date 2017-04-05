from django.conf.urls import url

from . import views

urlpatterns = [
    # This should list all
    url(r'^$', views.category_list, name='list'),
    # This should list all the subcategories associated with the given category
    url(r'^(?P<category_name>[\w]+)/$', views.category, name='category'),
    # This should not exist
    # url(r'^[\w]+/subcategory/[\w]+/interest_group/(?P<interest_group_name>[\w]+)', views.interest_group,
    #     name='interest_group'),
    # This should list the interest groups associated with the given subcategory
    url(r'^[\w]+/subcategory/(?P<subcategory_name>[\w]+)', views.subcategory, name='subcategory'),
]
