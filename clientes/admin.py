from django.contrib import admin
from .models import Cliente

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('cliente_id', 'edad', 'genero', 'saldo', 'activo', 'nivel_de_satisfaccion')
    search_fields = ('cliente_id', 'genero')
    list_filter = ('activo', 'genero', 'nivel_de_satisfaccion')
