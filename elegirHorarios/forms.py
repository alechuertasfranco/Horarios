from django import forms
from django.forms import fields
from .models import Curso 

class CursoForm(forms.ModelForm):
  
  class Meta:
    model=Curso 
    fields=['descripcion', 'id_usuario']