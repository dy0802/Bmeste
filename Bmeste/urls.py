from django.urls import path
from Bmeste import views

app_name = 'Bmeste'

urlpatterns = [
    path('', views.index, name='index'),
    path('pieces/', views.pieces, name='pieces'),
    path('authors/', views.authors, name='authors'),
]