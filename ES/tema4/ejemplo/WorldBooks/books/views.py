from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def saludo(request):
    datos = {
        "nombre": "Israel",
        "edad": 22,
        "ciudad": "Zafra",
    }
    return render (request, "books/saludo.html", context=datos)
