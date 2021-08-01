from django.urls import path, include
from elegirHorarios.views import *
from django.contrib.auth import views


urlpatterns = [
  # Mantenedor Profesor
  path('listarprofesor/', listarprofesor, name="listarprofesor"),
  path('agregarprofesor/', agregarprofesor, name="agregarprofesor"), 
  path('editarprofesor/<int:id>/', editarprofesor, name="editarprofesor"),
  path('eliminarprofesor/<int:id>/', eliminarprofesor, name="eliminarprofesor"),
  
  # Mantenedor Curso
  path('listarcurso/', listarcurso ,name="listarcurso"),
  path('agregarcurso/', agregarcurso, name="agregarcurso"), 
  path('editarcurso/<int:id>/', editarcurso, name="editarcurso"),
  path('eliminarcurso/<int:id>/', eliminarcurso, name="eliminarcurso"),
]