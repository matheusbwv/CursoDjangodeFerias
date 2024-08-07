from django.urls import path
from . import views

urlpatterns = [
  path("", views.index,name='produtos'),
  path("adicionar/", views.adicionar,name='produtos_add'),
  path("remover/", views.remover,name='produtos_deletar')
]