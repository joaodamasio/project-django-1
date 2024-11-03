from django.contrib import admin
from galeria.models import Fotografia

# Register your models here.
# https://docs.djangoproject.com/en/5.1/ref/contrib/admin/
# aqui personalizamos o nosso admin
class ListandoFotografias(admin.ModelAdmin):
    list_display = ("id", "nome","preco", "legenda","publicada")
    list_display_links = ("id","nome")
    search_fields = ("id", "nome")
    list_filter = ("categoria","usuarios",)
    list_editable= ("publicada",)#editar direto no display
    list_per_page = 20

# faz o registro das configuracoes
admin.site.register(Fotografia, ListandoFotografias)