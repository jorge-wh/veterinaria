from __future__ import absolute_import,unicode_literals
from django.conf.urls import url, include

from apps.adopcion.views import index_adopcion


urlpatterns = [
    url(r'^index$', index_adopcion),
]