from django.shortcuts import render
from django.http import HttpResponse

def hola(request):
    return HttpResponse("Hola. Plataforma de entregas (aún sin pedidos).")