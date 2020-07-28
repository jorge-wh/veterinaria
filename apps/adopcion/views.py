from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def index_adopcion(request):
        return HttpResponse("Estas en adopcion")