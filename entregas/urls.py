from django.urls import path
from . import views

urlpatterns = [
    path("hola/", views.hola, name="hola"),
    path("estado/", views.estado, name="estado"),
    path("visitas/", views.visitas, name="visitas"),
    path("visitas-mal/", views.visitas_mal, name="visitas_mal"),
    path("cotizar/", views.cotizar, name="cotizar"),
    path("cliente/", views.cliente, name="cliente"),
    path("ultimo-ok/", views.ultimo_ok, name="ultimo_ok"),
    path("ultimo-ok/ver/", views.ultimo_ok_ver, name="ultimo_ok_ver"),
]