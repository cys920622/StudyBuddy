from django.conf.urls import url
from .views import (posts_home, post_create, post_delete, post_detail, post_modify)


urlpatterns = [
    url(r'^$', posts_home, name="home"),
    url(r'^create/$', post_create, name="post_create"),
    url(r'^(?P<slug>[\w\-]+)/$', post_detail, name="post_detail"),
    url(r'^(?P<slug>[\w\-]+)/modify/$', post_modify, name="post_modify"),
    url(r'^(?P<slug>[\w\-]+)/delete/$', post_delete, name="post_delete"),
]