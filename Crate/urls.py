from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.category_list, name='list'),
    url(r'^(?P<category_name>[\w]+)/$', views.category, name='category'),
    url(r'^[\w]+/subcategory/(?P<subcategory_name>[\w]+)', views.subcategory, name='subcategory'),
    url(r'^(?P<box_id>[\d]+)/vote$', views.box_vote, name='box_item_vote'),
]
