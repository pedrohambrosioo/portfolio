from django.shortcuts import render

#o que vai ser exibido em cada tela

def index(request):
    return render(request, 'galeria/index.html')

def teste(request):
    return render(request, 'galeria/sobre.html')



