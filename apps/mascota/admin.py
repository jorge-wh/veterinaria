from __future__ import absolute_import,unicode_literals

from django.contrib import admin

from apps.mascota.models import Vacuna, Mascota 
# Register your models here.

admin.site.register(Vacuna)
admin.site.register(Mascota)

