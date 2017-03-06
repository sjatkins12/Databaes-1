from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<box_id>[\d]+)/$', views.box, name='box'),
]
