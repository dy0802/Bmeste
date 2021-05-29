from django.shortcuts import render

def index(request):
    return render(request, 'Bmeste/index.html')

def pieces(request):
    return render(request, 'Bmeste/pieces.html')

def authors(request):
    return render(request, 'Bmeste/authors.html')