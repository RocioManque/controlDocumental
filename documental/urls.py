from django.urls import path
from . import views

urlpatterns = [
    path('',views.inicio,name='inicio'),
    path('inicio',views.inicio,name='inicio'),
    path('documentos',views.documentos,name='documentos'),
    path('documentos/crear',views.crear,name='crear'),
    path('documentos/editar',views.editar,name='editar'),
    path('eliminar/<int:id>',views.eliminar,name='eliminar'),
    path('documentos/editar/<int:id>',views.editar,name='editar'),
    path('documentos/ver/<int:id>',views.ver,name='ver'),




]