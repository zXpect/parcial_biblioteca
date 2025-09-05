# API REST - Sistema de Gestión de Biblioteca

Una API REST desarrollada con Django REST Framework para la gestión completa de una biblioteca digital.

## Funcionalidades

### Gestión de Entidades
- Autores: CRUD completo con biografías opcionales
- Editoriales: Gestión con información de contacto
- Libros: Control de inventario con ISBN y metadatos
- Miembros: Registro de usuarios de la biblioteca
- Préstamos: Sistema de préstamo y devolución

### Características Avanzadas
- Búsquedas inteligentes: Por título, autor o editorial
- Filtros dinámicos: Por fechas, estados y categorías
- Validaciones robustas: ISBN, emails únicos, teléfonos válidos
- Relaciones optimizadas: Consultas eficientes con select_related
- Paginación automática: 20 elementos por página
- Panel de administración: Interfaz gráfica para gestión

## Tecnologías

- Framework: Django 4.2.7 + Django REST Framework 3.14.0
- Base de datos: PostgreSQL
- Lenguaje: Python 3.11+
- Autenticación: Django Auth (extensible)

## Instalación

1. Clonar repositorio  
```bash
git https://github.com/zXpect/parcial_biblioteca.git
cd parcial_biblioteca/biblioteca_proyecto
```

2. Configurar entorno  
```bash
python -m venv biblioteca_env
# Windows
biblioteca_env\Scripts\activate
# Linux/Mac
source biblioteca_env/bin/activate
```

3. Instalar dependencias  
```bash
pip install -r requirements.txt
```

4. Configurar PostgreSQL  
```sql
CREATE DATABASE biblioteca_db;
CREATE USER biblioteca_user WITH PASSWORD 'tu_password';
GRANT ALL PRIVILEGES ON DATABASE biblioteca_db TO biblioteca_user;
```

5. Variables de entorno  
```bash
# Crear archivo .env basado en .env.example
cp .env.example .env
# Editar con tus credenciales de PostgreSQL
```

6. Ejecutar migraciones  
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

7. Iniciar servidor  
```bash
python manage.py runserver
# API disponible en: http://localhost:8000/api/
```

## Endpoints API

### Autores (/api/autores/)
- GET - Listar todos los autores
- POST - Crear nuevo autor
- GET /{id}/ - Obtener autor específico
- PUT /{id}/ - Actualizar autor completo
- PATCH /{id}/ - Actualizar autor parcial
- DELETE /{id}/ - Eliminar autor

### Editoriales (/api/editoriales/)
- GET - Listar todas las editoriales
- POST - Crear nueva editorial
- GET /{id}/ - Obtener editorial específica
- PUT /{id}/ - Actualizar editorial completa
- PATCH /{id}/ - Actualizar editorial parcial
- DELETE /{id}/ - Eliminar editorial

### Libros (/api/libros/)
- GET - Listar todos los libros
- POST - Crear nuevo libro
- GET /{id}/ - Obtener libro específico
- PUT /{id}/ - Actualizar libro completo
- PATCH /{id}/ - Actualizar libro parcial
- DELETE /{id}/ - Eliminar libro

**Filtros disponibles:**
- ?autor=1 - Filtrar por autor
- ?editorial=1 - Filtrar por editorial
- ?año_publicacion=2023 - Filtrar por año
- ?search=titulo - Buscar por título

### Miembros (/api/miembros/)
- GET - Listar todos los miembros
- POST - Crear nuevo miembro
- GET /{id}/ - Obtener miembro específico
- PUT /{id}/ - Actualizar miembro completo
- PATCH /{id}/ - Actualizar miembro parcial
- DELETE /{id}/ - Eliminar miembro

### Préstamos (/api/prestamos/)
- GET - Listar todos los préstamos
- POST - Crear nuevo préstamo
- GET /{id}/ - Obtener préstamo específico
- PUT /{id}/ - Actualizar préstamo completo
- PATCH /{id}/ - Actualizar préstamo parcial
- DELETE /{id}/ - Eliminar préstamo
- PATCH /{id}/devolver/ - Devolver libro prestado

**Filtros disponibles:**
- ?miembro=1 - Filtrar por miembro
- ?fecha_prestamo=2024-01-15 - Filtrar por fecha
- ?activos=true - Solo préstamos activos
- ?activos=false - Solo préstamos devueltos

## Documentación API

Documentación completa con ejemplos: [Postman Documentation](https://documenter.getpostman.com/view/42853789/2sB3Hkq17d)

## Ejemplo de uso

Crear un autor:
```bash
curl -X POST http://localhost:8000/api/autores/ -H "Content-Type: application/json" -d '{"nombre": "Gabriel", "apellido": "García Márquez", "biografia": "Escritor colombiano"}'
```

Buscar libros por autor:
```bash
curl "http://localhost:8000/api/libros/?autor=1"
```

Crear préstamo:
```bash
curl -X POST http://localhost:8000/api/prestamos/ -H "Content-Type: application/json" -d '{"libro": 1, "miembro": 1}'
```

## Estructura del Proyecto

```
biblioteca-api/
├── biblioteca_proyecto/          # Configuración Django
│   ├── settings.py              # Configuración principal
│   └── urls.py                  # URLs principales
├── biblioteca/                   # App principal
│   ├── models.py                # Modelos de datos
│   ├── serializers.py           # Serializadores DRF
│   ├── views.py                 # Lógica de vistas
│   ├── urls.py                  # URLs de la API
│   └── admin.py                 # Configuración admin
├── requirements.txt             # Dependencias Python
├── .env.example                 # Plantilla variables entorno
└── README.md                    # Documentación
```

## Casos de Uso

- Bibliotecas digitales: Gestión completa de inventario
- Centros educativos: Control de préstamos estudiantiles
- Bibliotecas públicas: Administración de membresías
- Librerías: Control de stock y clientes
- Proyectos académicos: Base para sistemas más complejos

## Contribuir

1. Fork del repositorio
2. Crear rama feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit cambios (`git commit -m 'feat: agregar nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Crear Pull Request
