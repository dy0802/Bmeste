from django.shortcuts import render, get_object_or_404
from Bmeste.models import Author, Piece, Piece_detail


def index(request):
    return render(request, 'Bmeste/index.html')

def pieces(request):
    author_list = Author.objects.all().order_by('-pub_date')
    context = {'author_list': author_list}
    return render(request, 'Bmeste/pieces.html', context)

def piece_detail(request, piece_id):
    piece = get_object_or_404(Piece, pk=piece_id)
    return render(request, 'Bmeste/piece_detail.html', {'piece': piece})

def authors(request):
    return render(request, 'Bmeste/authors.html')
