from django.contrib import admin
from django.db import models
from django.db.models import Model
from django import forms
from django.conf import settings
from django.db import models

# Create your models here.
class Perfil(Model):
  nombres=models.CharField(max_length=40)
  apellidos=models.CharField(max_length=40)
  email=models.EmailField()
  username=models.CharField(max_length=20)
  password = models.CharField(max_length=50)
  telefono=models.CharField(max_length=9, null=True)
  estado=models.BooleanField(default=True)
  id_usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
  def __str__(self): return self.apellidos
  
class Profesor(Model):
  id_profesor=models.AutoField(primary_key=True, auto_created = True, serialize = False, verbose_name="id_profesor")
  nombres=models.CharField(max_length=40)
  apellidos=models.CharField(max_length=40)
  email=models.EmailField(null=True, blank=True)
  estado=models.BooleanField(default=True)
  id_usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
  def __str__(self): return self.apellidos
  
class Dia(Model):
  id_dia=models.AutoField(primary_key=True, auto_created=True, serialize = False, verbose_name="id_dia")
  descripcion=models.CharField(max_length=10)
  estado=models.BooleanField(default=True)
  def __str__(self): return self.descripcion
  
class Curso(Model):
  id_curso=models.AutoField(primary_key=True, auto_created = True, serialize = False, verbose_name="id_curso")
  descripcion=models.CharField(max_length=100)
  tipo=models.CharField(max_length=50, default='OBLIGATORIO')
  estado=models.BooleanField(default=True)
  id_usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
  def __str__(self): return self.descripcion

class Horario(Model):
  id_horario=models.AutoField(primary_key=True, auto_created = True, serialize = False, verbose_name="id_horario")
  estado=models.BooleanField(default=True)
  id_usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
  def __str__(self): return str(self.id_horario)
  
class Opcion(Model):
  id_opcion=models.AutoField(primary_key=True, auto_created = True, serialize = False, verbose_name="id_opcion")
  descripcion=models.CharField(max_length=1)
  id_curso = models.ForeignKey(Curso, on_delete=models.CASCADE, default=1)
  id_profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE, default=1)
  def __str__(self): return self.descripcion
  
class OpcionDia(Model):
  id_opcion_dia=models.AutoField(primary_key=True, auto_created = True, serialize = False, verbose_name="id_opcion_dia")
  id_opcion=models.ForeignKey(Opcion, on_delete=models.CASCADE, default=1)
  id_dia=models.ForeignKey(Dia, on_delete=models.CASCADE, default=1)
  hora_inicio=models.TimeField()
  hora_fin=models.TimeField()
  
class OpcionHorario(Model):
  id_opcion_horario=models.AutoField(primary_key=True, auto_created = True, serialize = False, verbose_name="id_opcion_horario")
  id_opcion=models.OneToOneField(Opcion, on_delete=models.CASCADE, default=1)
  id_horario=models.OneToOneField(Horario, on_delete=models.CASCADE, default=1)
  