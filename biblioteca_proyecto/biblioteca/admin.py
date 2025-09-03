from django.contrib import admin

# biblioteca/admin.py

from django.contrib import admin
from .models import Autor, Editorial, Libro, Miembro, Prestamo

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido']
    search_fields = ['nombre', 'apellido']
    list_filter = ['nombre']

@admin.register(Editorial)
class EditorialAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'direccion', 'telefono']
    search_fields = ['nombre']

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor', 'editorial', 'año_publicacion']
    list_filter = ['autor', 'editorial', 'año_publicacion']
    search_fields = ['titulo', 'isbn']

@admin.register(Miembro)
class MiembroAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'email', 'fecha_membresia']
    search_fields = ['nombre', 'apellido', 'email']
    list_filter = ['fecha_membresia']

@admin.register(Prestamo)
class PrestamoAdmin(admin.ModelAdmin):
    list_display = ['libro', 'miembro', 'fecha_prestamo', 'fecha_devolucion', 'esta_devuelto']
    list_filter = ['fecha_prestamo', 'fecha_devolucion']
    search_fields = ['libro__titulo', 'miembro__nombre']