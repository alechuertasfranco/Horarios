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
            Q(apellidos__icontains=queryset), estado=True, id_usuario = usuario.id).distinct()
    
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


# Mantenedor de Opciones
@login_required(login_url="/login/")
def listaropcion(request, id):
    curso = Curso.objects.get(id_curso=id)
    opcion = Opcion.objects.filter(id_curso = curso.id_curso)
    
    context = {'opcion': opcion, 'curso': curso, "username": request.user.username}
    return render(request, "opcion/listar.html", context)

@login_required(login_url="/login/")
def agregaropcion(request, id):    
    if request.method == "POST":
        post = request.POST.copy()
        post['id_curso'] = id
        
        try:
            _descripcion = Opcion.objects.filter(id_curso = id).order_by('-descripcion')[:1].get()
            _descripcion = ord(_descripcion.descripcion) + 1
            post['descripcion'] = chr(_descripcion)
        except:
            post['descripcion'] = 'a'
        
        request.POST = post
        
        form = OpcionForm(request.POST, request=request)
        if form.is_valid():
            form.save()
            return redirect("listaropcion", id)
    else:
        form = OpcionForm(request=request)
    context = {'form_opcion': form, 'curso': id, "username": request.user.username}
    return render(request, "opcion/agregar.html", context)

@login_required(login_url="/login/")
def editaropcion(request, id):
    opcion = Opcion.objects.get(id_opcion=id)
    if request.method == "POST":
        
        post = request.POST.copy()
        post['id_curso'] = opcion.id_curso
        request.POST = post
        
        form = OpcionForm(request.POST, instance=opcion, request=request)
        if form.is_valid():
            form.save()
            return redirect("listaropcion", id)
    else:
        form = OpcionForm(instance=opcion, request=request)
        form.fields['id_curso'].widget = forms.HiddenInput()
    context = {"form": form, "username": request.user.username}
    return render(request, "opcion/editar.html", context)

@login_required(login_url="/login/")
def eliminaropcion(request, id):
    opcion = Opcion.objects.get(id_opcion=id)
    id_curso = opcion.id_curso_id
    opcion.delete()
    return redirect("listaropcion", id_curso)


# Mantenedor de Horarios de Opcion
@login_required(login_url="/login/")
def listaropciondia(request, id):
    opcion = Opcion.objects.get(id_opcion=id)
    opcion_dia = OpcionDia.objects.filter(id_opcion = opcion.id_opcion)
    
    context = {'opcion': opcion, 'opcion_dia': opcion_dia, "username": request.user.username}
    return render(request, "opcion_dia/listar.html", context)

@login_required(login_url="/login/")
def agregaropciondia(request, id):
    opcion = Opcion.objects.get(id_opcion=id)
    if request.method == "POST":
        
        post = request.POST.copy()
        post['id_opcion'] = id
        request.POST = post
        
        logger.warning("IS POST")
        form = OpcionDiaForm(request.POST)
        logger.warning(form.errors)
        if form.is_valid():
            logger.warning("IS VALID")
            form.save()
        else:
            logger.warning("IS NOT VALID")
            logger.warning(form["id_opcion"])
        return redirect("listaropcion", opcion.id_curso.id_curso)
    else:
        logger.warning("IS NOT POST")
        form = OpcionDiaForm()
    context = {'form': form, 'opcion': opcion, "username": request.user.username}
    return render(request, "opcion_dia/agregar.html", context)

# @login_required(login_url="/login/")
# def editaropcion(request, id):
#     opcion = Opcion.objects.get(id_opcion=id)
#     if request.method == "POST":
        
#         post = request.POST.copy()
#         post['id_curso'] = opcion.id_curso
#         request.POST = post
        
#         form = OpcionForm(request.POST, instance=opcion)
#         if form.is_valid():
#             form.save()
#             return redirect("listaropcion", id)
#     else:
#         form = OpcionForm(instance=opcion)
#         form.fields['id_curso'].widget = forms.HiddenInput()
#     context = {"form": form, "username": request.user.username}
#     return render(request, "opcion/editar.html", context)

# @login_required(login_url="/login/")
# def eliminaropcion(request, id):
#     opcion = Opcion.objects.get(id_opcion=id)
#     id_curso = opcion.id_curso_id
#     opcion.delete()
#     return redirect("listaropcion", id_curso)
