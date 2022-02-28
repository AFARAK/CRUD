from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('autores/', views.listarAutores, name='autores'),
    path('autores/new', views.create_autor, name='new_autor'),
    path('autores/<id>/', views.detail_view, name='autor_detail'),
    path('autores/update/<id>/', views.update_autor, name='autor_update'),
    path('autores/delete/<id>/', views.delete_view, name='autor_delete'),

    path('libros/', views.listar_libros, name = 'libros'),
    path('libros/crear_libros', views.crear_libros, name = 'crear_libros'),
    path('libros/detalles_libros/<name>/', views.detalles_libros, name = 'detalles_libros'),
    path('libros/actualizar_libros/<name>/', views.actualizar_libros, name = 'actualizar_libros'),
    path('libros/eliminar_libros/<name>/', views.eliminar_libros , name = 'eliminar_libros')
]