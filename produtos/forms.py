from django import forms
from produtos.models import Produto

class ProdutoForm(forms.ModelForm):
  
  class Meta:
    model = Produto
    fields = ['name','price']