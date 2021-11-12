from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('erase_db', erase_db),
    re_path(r'^delete/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/(?P<day>[0-9]{1,2})', delete_data),
    re_path(r'(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/(?P<day>[0-9]{1,2})', weather),

]
