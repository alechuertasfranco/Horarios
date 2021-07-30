from django import forms
from elegirHorarios.forms import CursoForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from elegirHorarios.models import Curso
from django.db.models import Q
import logging
# Get an instance of a logger
logger = logging.getLogger(__name__)

# Create your views here.
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
        
        logger.error(request.POST)
        post = request.POST.copy()
        post['id_usuario'] = request.user.id
        request.POST = post
        logger.error(request.POST)
        
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
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            return redirect("listarcurso")
    else:
        form = CursoForm(instance=curso)
    context = {"form": form, "username": request.user.username}
    return render(request, "curso/editar.html", context)


@login_required(login_url="/login/")
def eliminarcurso(request, id):
    curso = Curso.objects.get(id_curso=id)
    curso.estado = False
    curso.save()
    return redirect("listarcurso")
