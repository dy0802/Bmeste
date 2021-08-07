from django.contrib import admin
from Bmeste.models import *

class PieceInline(admin.StackedInline):
    model = Piece
    extra = 1

class AuthorAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                  {'fields': ['name']}),
        (None,                  {'fields': ['name_rus']}),
        (None,                  {'fields': ['description']}),
        (None,                  {'fields': ['img']}),
        (None,                  {'fields': ['birth']}),
        (None,                  {'fields': ['death']}),
        ('Date information',    {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [PieceInline]

class Piece_detailInline(admin.StackedInline):
    model = Piece_detail
    extra = 3

class CommentInline(admin.StackedInline):
    model = Comment_piece

class PieceAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                  {'fields': ['title']}),
    ]
    inlines = [Piece_detailInline, CommentInline]

admin.site.register(Author, AuthorAdmin)
admin.site.register(Piece, PieceAdmin)
admin.site.register(Piece_detail)
admin.site.register(Comment_piece)

