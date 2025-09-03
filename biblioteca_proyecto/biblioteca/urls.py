# biblioteca/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # URLs para Autor
    path('autores/', views.AutorListCreateView.as_view(), name='autor-list-create'),
    path('autores/<int:pk>/', views.AutorDetailView.as_view(), name='autor-detail'),
    
    # URLs para Editorial
    path('editoriales/', views.EditorialListCreateView.as_view(), name='editorial-list-create'),
    path('editoriales/<int:pk>/', views.EditorialDetailView.as_view(), name='editorial-detail'),
    
    # URLs para Libro
    path('libros/', views.LibroListCreateView.as_view(), name='libro-list-create'),
    path('libros/<int:pk>/', views.LibroDetailView.as_view(), name='libro-detail'),
    
    # URLs para Miembro
    path('miembros/', views.MiembroListCreateView.as_view(), name='miembro-list-create'),
    path('miembros/<int:pk>/', views.MiembroDetailView.as_view(), name='miembro-detail'),
    
    # URLs para Prestamo
    path('prestamos/', views.PrestamoListCreateView.as_view(), name='prestamo-list-create'),
    path('prestamos/<int:pk>/', views.PrestamoDetailView.as_view(), name='prestamo-detail'),
    path('prestamos/<int:prestamo_id>/devolver/', views.devolver_libro, name='devolver-libro'),
]