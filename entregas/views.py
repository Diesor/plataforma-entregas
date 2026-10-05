from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import socket

COPIA = socket.gethostname()

visitas_en_memoria = 0

def hola(request):
    return HttpResponse("Hola. Plataforma de entregas (aún sin pedidos).")

def estado(request):
    return JsonResponse({
        "servicio": "Plataforma de entregas",
        "version": 1,
        "medios disponibles": ["camioneta", "moto", "bicicleta", "dron"],
    })

def visitas(request):
    request.session["visitas"] = request.session.get("visitas", 0) + 1
    return JsonResponse({
        "atendido_por": COPIA,
        "visitas": request.session["visitas"],
    })

def visitas_mal(request):
    global visitas_en_memoria
    visitas_en_memoria += 1
    return JsonResponse({
        "atendido_por": COPIA,
        "visitas": visitas_en_memoria,
    })