from django import forms
from django.forms.widgets import TextInput
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
  class Meta:
    model=Opcion
    fields=['descripcion', 'id_curso', 'id_profesor']
    labels = {
        'descripcion': ('Código'),
        'id_profesor': ('Profesor'),
    }
    widgets = {
      'descripcion': TextInput(attrs={'placeholder':"Ejemplo: a, b, c..."})
    }
    
class OpcionDiaForm(forms.ModelForm):
  class Meta:
    model=OpcionDia
    fields=['id_opcion', 'id_dia', 'hora_inicio', 'hora_fin']