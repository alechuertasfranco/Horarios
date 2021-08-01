# Generated by Django 3.2.4 on 2021-08-01 07:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id_curso', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='id_curso')),
                ('descripcion', models.CharField(max_length=100)),
                ('estado', models.BooleanField(default=True)),
                ('id_usuario', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Dia',
            fields=[
                ('id_dia', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='id_dia')),
                ('descripcion', models.CharField(max_length=10)),
                ('estado', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id_horario', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='id_horario')),
                ('estado', models.BooleanField(default=True)),
                ('id_usuario', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Opcion',
            fields=[
                ('id_opcion', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='id_opcion')),
                ('descripcion', models.CharField(max_length=1)),
                ('estado', models.BooleanField(default=True)),
                ('id_curso', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='elegirHorarios.curso')),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id_profesor', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='id_profesor')),
                ('nombres', models.CharField(max_length=40)),
                ('apellidos', models.CharField(max_length=40)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('estado', models.BooleanField(default=True)),
                ('id_usuario', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=40)),
                ('apellidos', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=9, null=True)),
                ('estado', models.BooleanField(default=True)),
                ('id_usuario', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OpcionHorario',
            fields=[
                ('id_opcion_horario', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='id_opcion_horario')),
                ('id_horario', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='elegirHorarios.horario')),
                ('id_opcion', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='elegirHorarios.opcion')),
            ],
        ),
        migrations.CreateModel(
            name='OpcionDia',
            fields=[
                ('id_opcion_dia', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='id_opcion_dia')),
                ('hora_inicio', models.TimeField()),
                ('hora_fin', models.TimeField()),
                ('id_dia', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='elegirHorarios.dia')),
                ('id_opcion', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='elegirHorarios.opcion')),
            ],
        ),
        migrations.AddField(
            model_name='opcion',
            name='id_profesor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='elegirHorarios.profesor'),
        ),
    ]
