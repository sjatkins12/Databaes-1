from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),  # Page about all items
    url(r'^(?P<item_id>[\d]+)/$', views.item, name='item'),  # /item/[id]/   => box_id = id, Page about single crate
]
