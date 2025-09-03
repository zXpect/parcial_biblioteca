# biblioteca/models.py

from django.db import models
from django.core.validators import RegexValidator

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    biografia = models.TextField(blank=True, null=True)
    
    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"
        ordering = ['apellido', 'nombre']
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Editorial(models.Model):
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=300)
    telefono = models.CharField(
        max_length=15, 
        blank=True, 
        null=True,
        validators=[RegexValidator(
            regex=r'^\+?1?\d{9,15}$',
            message="El teléfono debe tener entre 9 y 15 dígitos."
        )]
    )
    
    class Meta:
        verbose_name = "Editorial"
        verbose_name_plural = "Editoriales"
        ordering = ['nombre']
    
    def __str__(self):
        return self.nombre

class Libro(models.Model):
    titulo = models.CharField(max_length=300)
    resumen = models.TextField()
    isbn = models.CharField(
        max_length=13, 
        unique=True,
        validators=[RegexValidator(
            regex=r'^\d{13}$',
            message="ISBN debe tener exactamente 13 dígitos."
        )]
    )
    año_publicacion = models.PositiveIntegerField()
    
    # Relaciones
    autor = models.ForeignKey(
        Autor, 
        on_delete=models.CASCADE,
        related_name='libros'
    )
    editorial = models.ForeignKey(
        Editorial, 
        on_delete=models.CASCADE,
        related_name='libros'
    )
    
    class Meta:
        verbose_name = "Libro"
        verbose_name_plural = "Libros"
        ordering = ['titulo']
    
    def __str__(self):
        return self.titulo

class Miembro(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    fecha_membresia = models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Miembro"
        verbose_name_plural = "Miembros"
        ordering = ['apellido', 'nombre']
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Prestamo(models.Model):
    fecha_prestamo = models.DateField(auto_now_add=True)
    fecha_devolucion = models.DateField(blank=True, null=True)
    
    # Relaciones
    libro = models.ForeignKey(
        Libro, 
        on_delete=models.CASCADE,
        related_name='prestamos'
    )
    miembro = models.ForeignKey(
        Miembro, 
        on_delete=models.CASCADE,
        related_name='prestamos'
    )
    
    class Meta:
        verbose_name = "Préstamo"
        verbose_name_plural = "Préstamos"
        ordering = ['-fecha_prestamo']
    
    def __str__(self):
        return f"Préstamo de {self.libro.titulo} a {self.miembro}"
    
    @property
    def esta_devuelto(self):
        return self.fecha_devolucion is not None