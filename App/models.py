from django.db import models

class Publicacion(models.Model):
    titulo = models.TextField(max_length=100)
    precio = models.CharField(max_length=10)
    descripcion = models.TextField(max_length=1000)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.titulo} - {self.descripcion} - {self.precio} - {self.fecha_publicacion}"
