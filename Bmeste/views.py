from django.shortcuts import render
from Bmeste.models import Author, Pieces


def index(request):
    return render(request, 'Bmeste/index.html')

def pieces(request):
    author_list = Author.objects.all().order_by('-pub_date')
    context = {'author_list': author_list}
    return render(request, 'Bmeste/pieces.html', context)

def piece_detail(request):
    return render(request, 'Bmeste/piece_detail.html')

def authors(request):
    return render(request, 'Bmeste/authors.html')