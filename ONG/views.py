from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'core/index.html')

def gatos(request):
    return render(request, 'core/lista_gatos.html')

def perros(request):
    return render(request, 'core/lista_perros.html')

def cachulo(request):
    return render(request, 'core/cachulo.html')

def flaca(request):
    return render(request, 'core/flaca.html')

def ginger(request):
    return render(request, 'core/ginger.html')

def lucifer(request):
    return render(request, 'core/lucifer.html')

def nina(request):
    return render(request, 'core/nina.html')

def thommy(request):
    return render(request, 'core/thommy.html')

