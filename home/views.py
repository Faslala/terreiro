from django.shortcuts import render

def home(request):
    return render(request, 'home/home.html')

def historia(request):
    return render(request, 'home/historia.html')

def entrar(request):
    return render(request, 'home/entrar.html')

def hierarquia(request):
    return render(request, 'home/hierarquia.html')

def calendario(request):
    return render(request, 'home/calendario.html')

def banhos(request):
    return render(request, 'home/banhos.html')

def ervas(request):
    return render(request, 'home/ervas.html')
