from django.shortcuts import render, redirect
from produtos.models import Produto
from produtos.forms import ProdutoForm

# Create your views here.
def index(request):
  produtos = Produto.objects.all()
  return render(request,'produtos/index.html', {
    "produtos":produtos
  })

def adicionar(request):
  if request.method == 'POST':
    form = ProdutoForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('produtos')
  else: 
    form = ProdutoForm()
    return render(request,'produtos/adicionar.html',{
      'form':form
    })

def remover(request):
  pass