# Generated by Django 3.2.4 on 2021-09-28 03:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('elegirHorarios', '0004_alter_opcion_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opciondia',
            name='id_dia',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='elegirHorarios.dia'),
        ),
        migrations.AlterField(
            model_name='opciondia',
            name='id_opcion',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='elegirHorarios.opcion'),
        ),
    ]
