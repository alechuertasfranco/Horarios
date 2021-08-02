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
  
  # Mantenedor Opcion
  path('listaropcion/<int:id>/', listaropcion, name="listaropcion"),
  path('agregaropcion/<int:id>/', agregaropcion, name="agregaropcion"), 
  path('editaropcion/<int:id>/', editaropcion, name="editaropcion"),
  path('eliminaropcion/<int:id>/', eliminaropcion, name="eliminaropcion"),
  
  # Mantenedor Opcion_Dia
  path('listaropciondia/<int:id>/', listaropciondia, name="listaropciondia"),
  path('agregaropciondia/<int:id>/', agregaropciondia, name="agregaropciondia"), 
  # path('editaropciondia/<int:id>/', editaropciondia, name="editaropciondia"),
  # path('eliminaropciondia/<int:id>/', eliminaropciondia, name="eliminaropciondia"),
]