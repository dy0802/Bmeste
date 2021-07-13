from django.contrib import admin
from Bmeste.models import Author, Author_detail, Piece, Piece_detail, Comment_piece

admin.site.register(Author)
admin.site.register(Author_detail)
admin.site.register(Piece)
admin.site.register(Piece_detail)
admin.site.register(Comment_piece)