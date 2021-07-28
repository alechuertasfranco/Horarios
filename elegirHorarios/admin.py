from elegirHorarios.models import Curso, Dia, Horario, Opcion, OpcionDia, OpcionHorario, Profesor, Usuario
from django.contrib import admin

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id_usuario', 'nombres', 'apellidos', 'telefono')
class ProfesorAdmin(admin.ModelAdmin):
    list_display = ('id_profesor', 'nombres', 'apellidos')
class DiaAdmin(admin.ModelAdmin):
    list_display = ('id_dia', 'descripcion')
class CursoAdmin(admin.ModelAdmin):
    list_display = ('id_curso', 'descripcion')
class HorarioAdmin(admin.ModelAdmin):
    list_display = ('id_horario', 'id_usuario')
class OpcionAdmin(admin.ModelAdmin):
    list_display = ('id_opcion', 'descripcion')
class OpcionDiaAdmin(admin.ModelAdmin):
    list_display = ('id_opcion', 'id_dia', 'hora_inicio', 'hora_fin')
class OpcionHorarioAdmin(admin.ModelAdmin):
    list_display = ('id_opcion', 'id_horario')

# Register your models here.
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Profesor, ProfesorAdmin)    
admin.site.register(Dia, DiaAdmin)    
admin.site.register(Curso, CursoAdmin)    
admin.site.register(Horario, HorarioAdmin)    
admin.site.register(Opcion, OpcionAdmin)    
admin.site.register(OpcionDia, OpcionDiaAdmin)    
admin.site.register(OpcionHorario, OpcionHorarioAdmin)    

