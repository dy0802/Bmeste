from django.urls import path, re_path
from Bmeste import views

app_name = 'Bmeste'

urlpatterns = [
    path('', views.index, name='index'),
    path('pieces/', views.pieces, name='pieces'),
    re_path(r'^pieces/(?P<piece_id>\d+)/', views.piece_detail, name='piece_detail'),
    path('authors/', views.authors, name='authors'),
    re_path(r'^authors/(?P<author_id>\d+)/', views.author_detail, name='author_detail'),
]