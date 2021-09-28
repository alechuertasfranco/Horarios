from django import forms
from django.forms.models import ModelChoiceField
from django.forms.widgets import *
from .models import Curso, Opcion, OpcionDia, Profesor 

class CursoForm(forms.ModelForm):
  class Meta:
    model=Curso 
    fields=['descripcion', 'id_usuario']

class ProfesorForm(forms.ModelForm):
  class Meta:
    model=Profesor 
    fields=['apellidos', 'nombres', 'email', 'id_usuario']

class OpcionForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
    self.request = kwargs.pop("request")
    super(OpcionForm, self).__init__(*args, **kwargs)
    self.fields['id_profesor'].queryset = Profesor.objects.filter(id_usuario = self.request.user)
  class Meta:
    model=Opcion
    fields=['descripcion', 'id_curso', 'id_profesor']
    labels = {
        'id_profesor': ('Profesor'),
    }
    widgets = {
      'id_curso': HiddenInput(),
      'descripcion': HiddenInput()
    }
    
class OpcionDiaForm(forms.ModelForm):
  class Meta:
    model=OpcionDia
    fields=['id_opcion', 'id_dia', 'hora_inicio', 'hora_fin']
    labels = {
        'id_dia': ('Día'),
        'hora_inicio': ('Hora de incio'),
        'hora_fin': ('Hora de finalización'),
    }
    widgets = {
      'id_opcion': HiddenInput(),
    }