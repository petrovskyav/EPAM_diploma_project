from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf.urls import include
from weather_comparator.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('weather_comparator.urls')), # Корень пишется так
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
handler404 = pageNotFound
