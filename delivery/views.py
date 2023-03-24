from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html')


def clienti_page(request):
    return render(request, 'home.html')


def posta_page(request):
    return render(request, 'home.html')
