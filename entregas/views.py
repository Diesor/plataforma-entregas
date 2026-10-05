from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def hola(request):
    return HttpResponse("Hola. Plataforma de entregas (aún sin pedidos).")

def estado(request):
    return JsonResponse({
        "servicio": "Plataforma de entregas",
        "version": 1,
        "medios disponibles": ["camioneta", "moto", "bicicleta", "dron"],
    })