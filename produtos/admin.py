from django.contrib import admin
from produtos.models import Produto
# Register your models here.
class produtoAdmin(admin.ModelAdmin):
  list_display = ['name','price']

admin.site.register(Produto,produtoAdmin)