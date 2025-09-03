from django.shortcuts import render

# biblioteca/views.py

from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from django.db.models import Q

from .models import Autor, Editorial, Libro, Miembro, Prestamo
from .serializers import (
    AutorSerializer, EditorialSerializer, LibroSerializer,
    MiembroSerializer, PrestamoSerializer
)

# Vistas para Autor
class AutorListCreateView(generics.ListCreateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['nombre', 'apellido']
    ordering_fields = ['nombre', 'apellido']

class AutorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

# Vistas para Editorial
class EditorialListCreateView(generics.ListCreateAPIView):
    queryset = Editorial.objects.all()
    serializer_class = EditorialSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['nombre']
    ordering_fields = ['nombre']

class EditorialDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Editorial.objects.all()
    serializer_class = EditorialSerializer

# Vistas para Libro
class LibroListCreateView(generics.ListCreateAPIView):
    queryset = Libro.objects.select_related('autor', 'editorial')
    serializer_class = LibroSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['autor', 'editorial', 'año_publicacion']
    search_fields = ['titulo', 'autor__nombre', 'autor__apellido', 'editorial__nombre']
    ordering_fields = ['titulo', 'año_publicacion']

class LibroDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Libro.objects.select_related('autor', 'editorial')
    serializer_class = LibroSerializer

# Vistas para Miembro
class MiembroListCreateView(generics.ListCreateAPIView):
    queryset = Miembro.objects.all()
    serializer_class = MiembroSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['nombre', 'apellido', 'email']
    ordering_fields = ['nombre', 'apellido', 'fecha_membresia']

class MiembroDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Miembro.objects.all()
    serializer_class = MiembroSerializer

# Vistas para Prestamo
class PrestamoListCreateView(generics.ListCreateAPIView):
    queryset = Prestamo.objects.select_related('libro', 'miembro')
    serializer_class = PrestamoSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['miembro', 'libro', 'fecha_prestamo']
    search_fields = ['libro__titulo', 'miembro__nombre', 'miembro__apellido']
    ordering_fields = ['fecha_prestamo', 'fecha_devolucion']
    
    def get_queryset(self):
        queryset = super().get_queryset()
        # Filtro para préstamos activos (no devueltos)
        activos = self.request.query_params.get('activos', None)
        if activos == 'true':
            queryset = queryset.filter(fecha_devolucion__isnull=True)
        elif activos == 'false':
            queryset = queryset.filter(fecha_devolucion__isnull=False)
        
        return queryset

class PrestamoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Prestamo.objects.select_related('libro', 'miembro')
    serializer_class = PrestamoSerializer

# Vista especial para devolver un libro
@api_view(['PATCH'])
def devolver_libro(request, prestamo_id):
    try:
        prestamo = Prestamo.objects.get(id=prestamo_id)
        if prestamo.fecha_devolucion:
            return Response(
                {'error': 'Este libro ya ha sido devuelto'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        from django.utils import timezone
        prestamo.fecha_devolucion = timezone.now().date()
        prestamo.save()
        
        serializer = PrestamoSerializer(prestamo)
        return Response(serializer.data)
        
    except Prestamo.DoesNotExist:
        return Response(
            {'error': 'Préstamo no encontrado'},
            status=status.HTTP_404_NOT_FOUND
        )