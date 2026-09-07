from django.db import models

class Autor(models.Model):
    nombre= models.CharField(max_length=100)
    nacionalidad= models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
class Categoria(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre
    
class Libro(models.Model):
    titulo = models.CharField(max_length=200) 
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name="libros") 
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, related_name="libros") 
    anio_publicacion = models.IntegerField() 
    stock = models.PositiveBigIntegerField(default=0) 
    precio = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.titulo
    

class Socio(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    fecha_inscripcion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre


class Arriendo(models.Model):  
    socio = models.ForeignKey(Socio, on_delete=models.CASCADE) 
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE) 
    fecha_arriendo = models.DateTimeField(auto_now_add=True)
    fecha_devolucion = models.DateField(null=True, blank=True)
    devuelto = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.socio} - {self.libro}"
