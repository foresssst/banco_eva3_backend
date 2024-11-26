from django.urls import path
from . import views
from .views import ClienteListCreateView
from .views import ClienteListView, ClienteCreateView, ClienteUpdateView, ClienteDeleteView, cliente_stats_view

urlpatterns = [
    path('clientes/', ClienteListCreateView.as_view(), name='clientes-list-create'),
    path('', ClienteListView.as_view(), name='cliente-list'),
    path('create/', ClienteCreateView.as_view(), name='cliente-create'),
    path('update/<int:pk>/', ClienteUpdateView.as_view(), name='cliente-update'),
    path('delete/<int:pk>/', ClienteDeleteView.as_view(), name='cliente-delete'),
    path('stats/', views.cliente_stats_view, name='cliente-stats'),
]