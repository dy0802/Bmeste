from django.urls import path, re_path
from Bmeste import views

app_name = 'Bmeste'

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^author/(?P<author_id>\d+)/', views.pieces, name='pieces'),
    re_path(r'^pieces/(?P<piece_id>\d+)/', views.piece_detail, name='piece_detail'),
    re_path(r'^pieces/c_post/(?P<piece_id>\d+)/', views.c_post, name="c_post"),
    path('pieces/all/', views.all_pieces, name='all_pieces'),
    path('authors/', views.authors, name='authors'),
    path('about/', views.about, name='about'),
    re_path(r'^authors/(?P<author_id>\d+)/', views.author_detail, name='author_detail'),
]