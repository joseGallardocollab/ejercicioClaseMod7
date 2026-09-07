from django.contrib import admin
from .models import Autor, Categoria, Libro, Socio, Arriendo

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'nacionalidad']   
    search_fields = ['nombre']                  
    list_filter = ['nacionalidad']              

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    search_fields = ['nombre']

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = [
        'titulo',
        'autor',
        'categoria',
        'anio_publicacion',
        'stock',
        'precio'
    ]
    search_fields = ['titulo', 'autor__nombre', 'categoria__nombre']
    list_filter = ['categoria', 'autor', 'anio_publicacion']

@admin.register(Socio)
class SocioAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'email', 'fecha_inscripcion']
    search_fields = ['nombre']
    list_filter = ['nombre']  


@admin.register(Arriendo)
class ArriendoAdmin(admin.ModelAdmin):
    list_display = ['socio', 'libro', 'fecha_arriendo', 'fecha_devolucion','devuelto' ]
    search_fields = [  'socio', 'devuelto' ]
    list_filter = ['socio', 'libro', 'fecha_arriendo', 'fecha_devolucion','devuelto'] 

    list_per_page = 25