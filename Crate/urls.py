from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<box_id>[\d]+)/vote$', views.box_vote, name='box_item_vote'),
]
