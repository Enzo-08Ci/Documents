from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1>Essa view é de teste</h1>")

def contatos(request):
    return HttpResponse("<p>telefone:(21)973171269</p><p>Email:enzo.franca008@gmail.com")

