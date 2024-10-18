from django.urls import path
from galeria.views import index, imagem
from . import views

urlpatterns = [
    path('', index, name='index'),
    path('imagem/', imagem, name='imagem')
]