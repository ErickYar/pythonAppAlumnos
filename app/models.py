from django.db import models

# Create your models here.
class Estudiante(models.Model):
  codigo = models.PositiveIntegerField()
  nombre = models.CharField(max_length=50)
  apellidos = models.CharField(max_length=50)
  edad=models.IntegerField()
  email = models.EmailField(max_length=100)
  carrera = models.CharField(max_length=50)
  

  def __str__(self):
    return f'Estudiante: {self.nombre} {self.apellidos}'