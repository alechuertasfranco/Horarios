from django import forms
from .models import Curso, Profesor 

class CursoForm(forms.ModelForm):
  
  class Meta:
    model=Curso 
    fields=['descripcion', 'id_usuario']
class ProfesorForm(forms.ModelForm):
  class Meta:
    model=Profesor 
    fields=['apellidos', 'nombres', 'email', 'id_usuario']