from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.crate_home, name='crate_home'),  # /crate/        => Page about all crates (previous too)
    url(r'^(?P<box_id>[\d]+)/$', views.box, name='box'),  # /crate/[id]/   => box_id = id, Page about single crate
    url(r'^previous/$', views.previous, name='previous'),  # /crate/previous/ => Page listing all the previous boxes
]
