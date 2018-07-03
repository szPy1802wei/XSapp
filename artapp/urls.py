from django.conf.urls import url
from artapp.views import *


urlpatterns = [
    url(r'^tags', edit_tags),
    url(r'^list_tags', list_tags),
    url(r'^delete_tag', delete_tag),
    url(r'^show_detail', show_detail),
    url('^index', index, name='art'),


]