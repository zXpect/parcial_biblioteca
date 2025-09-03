# biblioteca/serializers.py

from rest_framework import serializers
from .models import Autor, Editorial, Libro, Miembro, Prestamo

class AutorSerializer(serializers.ModelSerializer):
    libros_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Autor
        fields = ['id', 'nombre', 'apellido', 'biografia', 'libros_count']
    
    def get_libros_count(self, obj):
        return obj.libros.count()

class EditorialSerializer(serializers.ModelSerializer):
    libros_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Editorial
        fields = ['id', 'nombre', 'direccion', 'telefono', 'libros_count']
    
    def get_libros_count(self, obj):
        return obj.libros.count()

class LibroSerializer(serializers.ModelSerializer):
    autor_nombre = serializers.StringRelatedField(source='autor', read_only=True)
    editorial_nombre = serializers.StringRelatedField(source='editorial', read_only=True)
    prestamos_activos = serializers.SerializerMethodField()
    
    class Meta:
        model = Libro
        fields = [
            'id', 'titulo', 'resumen', 'isbn', 'año_publicacion',
            'autor', 'autor_nombre', 'editorial', 'editorial_nombre',
            'prestamos_activos'
        ]
    
    def get_prestamos_activos(self, obj):
        return obj.prestamos.filter(fecha_devolucion__isnull=True).count()

class MiembroSerializer(serializers.ModelSerializer):
    prestamos_activos = serializers.SerializerMethodField()
    total_prestamos = serializers.SerializerMethodField()
    
    class Meta:
        model = Miembro
        fields = [
            'id', 'nombre', 'apellido', 'email', 'fecha_membresia',
            'prestamos_activos', 'total_prestamos'
        ]
    
    def get_prestamos_activos(self, obj):
        return obj.prestamos.filter(fecha_devolucion__isnull=True).count()
    
    def get_total_prestamos(self, obj):
        return obj.prestamos.count()

class PrestamoSerializer(serializers.ModelSerializer):
    libro_titulo = serializers.StringRelatedField(source='libro', read_only=True)
    miembro_nombre = serializers.SerializerMethodField()
    esta_devuelto = serializers.ReadOnlyField()
    
    class Meta:
        model = Prestamo
        fields = [
            'id', 'fecha_prestamo', 'fecha_devolucion',
            'libro', 'libro_titulo', 'miembro', 'miembro_nombre',
            'esta_devuelto'
        ]
    
    def get_miembro_nombre(self, obj):
        return str(obj.miembro)
    
    def validate(self, data):
        # Validar que el libro no esté ya prestado
        if not data.get('fecha_devolucion'):
            libro = data.get('libro')
            if libro and libro.prestamos.filter(fecha_devolucion__isnull=True).exists():
                raise serializers.ValidationError(
                    "Este libro ya está prestado y no ha sido devuelto."
                )
        return data