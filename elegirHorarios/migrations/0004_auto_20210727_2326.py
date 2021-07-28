# Generated by Django 3.2.4 on 2021-07-28 04:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('elegirHorarios', '0003_alter_usuario_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id_curso', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='id_curso')),
                ('descripcion', models.CharField(max_length=100)),
                ('estado', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Dia',
            fields=[
                ('id_dia', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='id_dia')),
                ('descripcion', models.CharField(max_length=10)),
                ('estado', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id_horario', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='id_horario')),
                ('estado', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Opcion',
            fields=[
                ('id_opcion', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='id_opcion')),
                ('descripcion', models.CharField(max_length=1)),
                ('id_curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elegirHorarios.curso')),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id_profesor', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='id_profesor')),
                ('nombres', models.CharField(max_length=40)),
                ('apellidos', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('estado', models.BooleanField()),
            ],
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='id',
            new_name='id_usuario',
        ),
        migrations.CreateModel(
            name='OpcionHorario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hora_inicio', models.TimeField()),
                ('hora_fin', models.TimeField()),
                ('id_horario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='elegirHorarios.horario')),
                ('id_opcion', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='elegirHorarios.opcion')),
            ],
        ),
        migrations.CreateModel(
            name='OpcionDia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hora_inicio', models.TimeField()),
                ('hora_fin', models.TimeField()),
                ('id_dia', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='elegirHorarios.dia')),
                ('id_opcion', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='elegirHorarios.opcion')),
            ],
        ),
        migrations.AddField(
            model_name='opcion',
            name='id_profesor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elegirHorarios.profesor'),
        ),
        migrations.AddField(
            model_name='horario',
            name='id_usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elegirHorarios.usuario'),
        ),
        migrations.AddField(
            model_name='curso',
            name='id_usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elegirHorarios.usuario'),
        ),
    ]
