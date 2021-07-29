from django.urls import path, include
from elegirHorarios.views import agregarcurso, editarcurso, eliminarcurso, listarcurso
from django.contrib.auth import views

urlpatterns = [
  path('listarcurso/', listarcurso ,name="listarcurso"),
  path('agregarcurso/', agregarcurso, name="agregarcurso"), 
  path('editarcurso/<int:id>/', editarcurso, name="editarcurso"),
  path('eliminarcurso/<int:id>/', eliminarcurso, name="eliminarcurso"),
]