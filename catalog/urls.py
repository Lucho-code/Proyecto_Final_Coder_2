from django.urls import path
from catalog import views
from Biblioteca import views

urlpatterns = [
    path('', views.index, name='inicio'),
    path('usuarios', views.usuario, name='usuarios'),
    path('administrativos', views.administrativos, name='administrativos'),
    path('registrarse', views.registrarse, name='registrarse'),
    path('contacto', views.contacto, name='contacto'),
]












#path('cargar_libro/', Cargar_libro.as_view(), name = 'cargar_libro'),