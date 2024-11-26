from rest_framework import generics
from .models import Cliente
from .serializers import ClienteSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.db.models import Avg, Count
from django.shortcuts import render
from django.http import JsonResponse

class ClienteListCreateView(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['activo', 'genero', 'nivel_de_satisfaccion']
    
class ClienteListView(ListView):
    model = Cliente
    template_name = 'clientes/cliente_list.html'

class ClienteCreateView(CreateView):
    model = Cliente
    fields = ['cliente_id', 'edad', 'genero', 'saldo', 'activo', 'nivel_de_satisfaccion']
    template_name = 'clientes/cliente_form.html'
    success_url = reverse_lazy('cliente-list')

class ClienteUpdateView(UpdateView):
    model = Cliente
    fields = ['cliente_id', 'edad', 'genero', 'saldo', 'activo', 'nivel_de_satisfaccion']
    template_name = 'clientes/cliente_form.html'
    success_url = reverse_lazy('cliente-list')

class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'clientes/cliente_confirm_delete.html'
    success_url = reverse_lazy('cliente-list')
    
def cliente_stats_view(request):
    # Calcular estadísticas básicas
    total_clientes = Cliente.objects.count()
    promedio_saldo = Cliente.objects.aggregate(promedio=Avg('saldo'))['promedio']
    distribucion_edades = list(Cliente.objects.values('edad').annotate(total=Count('edad')).order_by('edad'))
    proporcion_generos = list(Cliente.objects.values('genero').annotate(total=Count('genero')))
    promedio_satisfaccion = Cliente.objects.aggregate(promedio=Avg('nivel_de_satisfaccion'))['promedio']
    
    # Preparar datos para JSON
    data = {
        "total_clientes": total_clientes,
        "promedio_saldo": promedio_saldo,
        "promedio_satisfaccion": promedio_satisfaccion,
        "distribucion_edades": distribucion_edades,
        "proporcion_generos": proporcion_generos,
    }

    return JsonResponse(data)