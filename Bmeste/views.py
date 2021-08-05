from django.shortcuts import render, get_object_or_404, redirect
from Bmeste.models import Author, Piece, Comment_piece
from django.utils import timezone


def index(request):
    author_list = Author.objects.all()
    context = {'author_list': author_list}
    return render(request, 'Bmeste/index.html', context)

def all_pieces(request):
    author_list = Author.objects.all().order_by('-pub_date')
    context = {'author_list': author_list}
    return render(request, 'Bmeste/all_pieces.html', context)

def pieces(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    context = {'author': author}
    return render(request, 'Bmeste/pieces.html', context)

def piece_detail(request, piece_id):
    piece = get_object_or_404(Piece, pk=piece_id)
    comments = piece.comments.all()
    context = {'piece': piece, 'comments': comments}
    return render(request, 'Bmeste/piece_detail.html', context)

def c_post(request, piece_id):
    if request.method =='POST':
        piece = get_object_or_404(Piece, pk=piece_id)
        comment_text = request.POST.get('comment_text')
        comment_user = request.POST.get('comment_user')
        Comment_piece.objects.create(piece=piece, comment_text=comment_text, comment_user=comment_user)

    return redirect('Bmeste:piece_detail', piece_id)


def authors(request):
    return render(request, 'Bmeste/authors.html')

def about(request):
    return render(request, 'Bmeste/about.html')    

def author_detail(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    return render(request, 'Bmeste/author_detail.html', {'author': author})