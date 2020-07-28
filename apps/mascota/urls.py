from __future__ import absolute_import,unicode_literals
from django.conf.urls import url, include

from apps.mascota.views import index_mascota, mascota_view, mascota_list, mascota_edit, mascota_delete, \
    MascotaList, MascotaCreate, MascotaUpdate, MascotaDelete

app_name = 'mascota'

# Vistas a base de funciones
# urlpatterns = [
#     url(r'^$',                              index_mascota,  name='index'),
#     url(r'^nuevo$',                         MascotaCreate.as_view(),   name='mascota_crear'),
#     url(r'^listar$',                        MascotaList.as_view(),   name='mascota_listar'),
#     url(r'^editar/(?P<id_mascota>\d+)/$',   mascota_edit,   name='mascota_editar'),
#     url(r'^eliminar/(?P<id_mascota>\d+)/$', mascota_delete, name='mascota_eliminar'),
# ]

# Vistas a base de clases
urlpatterns = [
    url(r'^$',                              index_mascota,  name='index'),
    url(r'^nuevo$',                         MascotaCreate.as_view(),   name='mascota_crear'),
    url(r'^listar',                        MascotaList.as_view(),   name='mascota_listar'),
    url(r'^editar/(?P<pk>\d+)/$',           MascotaUpdate.as_view(),   name='mascota_editar'),
    url(r'^eliminar/(?P<pk>\d+)/$',         MascotaDelete.as_view(), name='mascota_eliminar'),
]