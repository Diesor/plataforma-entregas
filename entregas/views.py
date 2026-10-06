from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import socket
import math
from .reglas import elegir_medio

COPIA = socket.gethostname()

visitas_en_memoria = 0

ultimo_folio = None

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

def cotizar(request):
    km_txt = request.GET.get("km")
    kg_txt = request.GET.get("kg")

    if km_txt is None or kg_txt is None:
        return JsonResponse({"error": "Faltan los datos km y kg"}, status=400)

    try:
        km = float(km_txt)
        kg = float(kg_txt)
    except ValueError:
        return JsonResponse({"error": "km y kg deben ser numeros"}, status=400)

    if not (math.isfinite(km) and math.isfinite(kg)) or km < 0 or kg < 0:
        return JsonResponse({"error": "km y kg deben ser numeros positivos"}, status=400)

    medio, motivo = elegir_medio(km, kg)
    return JsonResponse({"km": km, "kg": kg, "medio": medio, "motivo": motivo})

def cliente(request):
    return render(request, "entregas/cliente.html")

def ultimo_ok(request):
    request.session["ultimo_folio"] = request.GET.get("folio")
    return JsonResponse({
        "guardado": request.session["ultimo_folio"],
        "atendido_por": COPIA,
    })


def ultimo_ok_ver(request):
    return JsonResponse({
        "ultimo_folio": request.session.get("ultimo_folio"),
        "atendido_por": COPIA,
    })