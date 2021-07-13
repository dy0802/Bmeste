from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from Bmeste.models import Author, Piece, Comment_piece
from django.utils import timezone


def index(request):
    return render(request, 'Bmeste/index.html')

def pieces(request):
    author_list = Author.objects.all().order_by('-pub_date')
    context = {'author_list': author_list}
    return render(request, 'Bmeste/pieces.html', context)

def piece_detail(request, piece_id):
    piece = get_object_or_404(Piece, pk=piece_id)
    if request.method == "POST":
        comment = Comment_piece()
        comment.post = piece
        comment.writer_name = request.POST['writer_name']
        comment.comment_text = request.POST['comment_text']
        comment.created = timezone.now
        comment.save()
    return render(request, 'Bmeste/piece_detail.html', {'piece': piece})

def authors(request):
    author_list = Author.objects.all().order_by('-pub_date')
    context = {'author_list': author_list}
    return render(request, 'Bmeste/authors.html', context)

def author_detail(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    return render(request, 'Bmeste/author_detail.html', {'author': author})