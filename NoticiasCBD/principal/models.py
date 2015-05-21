from django.db import models

# Create your models here.

class Persona(models.Model):
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    
    def __unicode__(self):
        return self.nombre +' ' + self.apellidos
    
class Noticia(models.Model):
    titulo = models.CharField(max_length=50)
    cuerpo = models.TextField()
    fecha_pub = models.DateTimeField(auto_now=True)
    # Relaciones
    publicador = models.ForeignKey(Persona)
    
    def __unicode__(self):
        return self.titulo
    
class Editorial(models.Model):
    nombre = models.CharField(max_length=30)
    #Relaciones
    empleados = models.ManyToManyField(Persona)
    
    def __unicode__(self):
        return self.nombre