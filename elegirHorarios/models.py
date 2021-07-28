from django.contrib import admin
from django.db import models
from django.db.models import Model
from django import forms

# Create your models here.
class Usuario(Model):
  id_usuario=models.AutoField(primary_key=True, auto_created = True, serialize = False, verbose_name="id_usuario")
  nombres=models.CharField(max_length=40)
  apellidos=models.CharField(max_length=40)
  telefono=models.CharField(max_length=9, null=True)
  email=models.EmailField()
  username=models.CharField(max_length=20)
  password = models.CharField(max_length=50)
  estado=models.BooleanField(default=True)
  def __str__(self): return self.apellidos
  
class Profesor(Model):
  id_profesor=models.AutoField(primary_key=True, auto_created = True, serialize = False, verbose_name="id_profesor")
  nombres=models.CharField(max_length=40)
  apellidos=models.CharField(max_length=40)
  email=models.EmailField(null=True)
  estado=models.BooleanField(default=True)
  def __str__(self): return self.apellidos
  
class Dia(Model):
  id_dia=models.AutoField(primary_key=True, auto_created=True, serialize = False, verbose_name="id_dia")
  descripcion=models.CharField(max_length=10)
  estado=models.BooleanField(default=True)
  def __str__(self): return self.descripcion
  
class Curso(Model):
  id_curso=models.AutoField(primary_key=True, auto_created = True, serialize = False, verbose_name="id_curso")
  descripcion=models.CharField(max_length=100)
  estado=models.BooleanField(default=True)
  id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
  def __str__(self): return self.descripcion

class Horario(Model):
  id_horario=models.AutoField(primary_key=True, auto_created = True, serialize = False, verbose_name="id_horario")
  estado=models.BooleanField(default=True)
  id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
  def __str__(self): return str(self.id_horario)
  
class Opcion(Model):
  id_opcion=models.AutoField(primary_key=True, auto_created = True, serialize = False, verbose_name="id_opcion")
  descripcion=models.CharField(max_length=1)
  estado=models.BooleanField(default=True)
  id_curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
  id_profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
  def __str__(self): return self.descripcion
  
class OpcionDia(Model):
  unique_together = (('id_opcion', 'id_dia'),)
  id_opcion=models.OneToOneField(Opcion, on_delete=models.CASCADE)
  id_dia=models.OneToOneField(Dia, on_delete=models.CASCADE)
  hora_inicio=models.TimeField()
  hora_fin=models.TimeField()
  
class OpcionHorario(Model):
  unique_together = (('id_opcion', 'id_horario'),)
  id_opcion=models.OneToOneField(Opcion, on_delete=models.CASCADE)
  id_horario=models.OneToOneField(Horario, on_delete=models.CASCADE)
  