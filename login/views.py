from typing import Generic 
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from elegirHorarios.models import *

# Create your views here.
def acceder(request):
  if request.method=="POST":
    form=AuthenticationForm(request,data=request.POST)
    
    if form.is_valid():
      nombre_usuario=form.cleaned_data.get("username")
      password=form.cleaned_data.get("password")
      usuario=authenticate(username=nombre_usuario,password=password)
      
      if usuario is not None:
        login(request,usuario)
        return redirect("home")
      else:
        messages.error(request, "Usuario y/o contraseña incorrectos")
        
    else:
      messages.error(request, "Datos invalidos")
      
  form=AuthenticationForm()
  return render(request, "login.html", {"form":form})

@login_required(login_url="/login/")
def salir(request):
  logout(request)
  messages.info(request,"Saliste exitosamente")
  return redirect("login")

@login_required(login_url="/login/")
def home(request):
  cursos = Curso.objects.filter(id_usuario=request.user, tipo='OBLIGATORIO')
  aux_opciones = {}
  max_opciones = {}
  horarios = []
  combinaciones = 1
  for _curso in cursos:
    opciones = Opcion.objects.filter(id_curso = _curso.id_curso)
    combinaciones *= len(opciones)
    aux_opciones[str(_curso.id_curso)] = 0
    max_opciones[str(_curso.id_curso)] = len(opciones)
  
  print(combinaciones)
  for i in range(10):
    for _curso in cursos:
      opciones = Opcion.objects.filter(id_curso = _curso.id_curso)
      for _opcion in opciones:
        _horario = []
        _opcion_curso = {'id_curso': _opcion.id_curso, 'id_opcion':_opcion.descripcion}
        if not horarios:
          _horario.append(_opcion_curso)
          horarios.append(_horario)
        else:
          _horario_exists = False
          for _item_horario in horarios:
            _opcion_exists = False
            for _item_opcion_curso in _item_horario:
              if _item_opcion_curso['id_curso'] == _opcion_curso['id_curso']:
                _opcion_exists = True
                break              
            if _opcion_exists:
              pass
            else:
              _item_horario.append(_opcion_curso)
              _horario_exists = True
          if not _horario_exists:
            _horario.append(_opcion_curso)
            horarios.append(_horario)
        
  context={'horarios': horarios,"username": request.user.username}
  return render(request, "home.html", context)