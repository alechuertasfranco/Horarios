from django import forms
from elegirHorarios.forms import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from elegirHorarios.models import *
from django.db.models import Q
import logging
# Get an instance of a logger
logger = logging.getLogger(__name__)

# Mantenedor de Profesores
@login_required(login_url="/login/")
def listarprofesor(request):
    usuario = request.user
    queryset = request.GET.get("buscar")
    profesor = Profesor.objects.filter(estado=True, id_usuario = usuario.id)
    if queryset:
        profesor = Profesor.objects.filter(
            Q(descripcion__icontains=queryset), estado=True, id_usuario = usuario.id).distinct()
    
    context = {'profesor': profesor, "username": usuario.username}
    return render(request, "profesor/listar.html", context)

@login_required(login_url="/login/")
def agregarprofesor(request):
    if request.method == "POST":
        
        post = request.POST.copy()
        post['id_usuario'] = request.user.id
        request.POST = post
        
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listarprofesor")
    else:
        form = ProfesorForm()
        form.fields['id_usuario'].widget = forms.HiddenInput()
    context = {'form': form, "username": request.user.username}
    return render(request, "profesor/agregar.html", context)

@login_required(login_url="/login/")
def editarprofesor(request, id):
    profesor = Profesor.objects.get(id_profesor=id)
    if request.method == "POST":
        
        post = request.POST.copy()
        post['id_usuario'] = request.user.id
        request.POST = post
        
        form = ProfesorForm(request.POST, instance=profesor)
        if form.is_valid():
            form.save()
            return redirect("listarprofesor")
    else:
        form = ProfesorForm(instance=profesor)
        form.fields['id_usuario'].widget = forms.HiddenInput()
    context = {"form": form, "username": request.user.username}
    return render(request, "profesor/editar.html", context)

@login_required(login_url="/login/")
def eliminarprofesor(request, id):
    profesor = Profesor.objects.get(id_profesor=id)
    profesor.estado = False
    profesor.save()
    return redirect("listarprofesor")


# Mantenedor de Cursos
@login_required(login_url="/login/")
def listarcurso(request):
    usuario = request.user
    queryset = request.GET.get("buscar")
    curso = Curso.objects.filter(estado=True, id_usuario = usuario.id)
    if queryset:
        curso = Curso.objects.filter(
            Q(descripcion__icontains=queryset), estado=True, id_usuario = usuario.id).distinct()
    
    context = {'curso': curso, "username": usuario.username}
    return render(request, "curso/listar.html", context)

@login_required(login_url="/login/")
def agregarcurso(request):
    if request.method == "POST":
        
        post = request.POST.copy()
        post['id_usuario'] = request.user.id
        request.POST = post
        
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listarcurso")
    else:
        form = CursoForm()
        form.fields['id_usuario'].widget = forms.HiddenInput()
    context = {'form': form, "username": request.user.username}
    return render(request, "curso/agregar.html", context)

@login_required(login_url="/login/")
def editarcurso(request, id):
    curso = Curso.objects.get(id_curso=id)
    if request.method == "POST":
        
        post = request.POST.copy()
        post['id_usuario'] = request.user.id
        request.POST = post
        
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            return redirect("listarcurso")
    else:
        form = CursoForm(instance=curso)
        form.fields['id_usuario'].widget = forms.HiddenInput()
    context = {"form": form, "username": request.user.username}
    return render(request, "curso/editar.html", context)

@login_required(login_url="/login/")
def eliminarcurso(request, id):
    curso = Curso.objects.get(id_curso=id)
    curso.estado = False
    curso.save()
    return redirect("listarcurso")
