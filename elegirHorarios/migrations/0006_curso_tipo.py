# Generated by Django 3.2.4 on 2021-10-01 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elegirHorarios', '0005_auto_20210927_2202'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='tipo',
            field=models.CharField(default='OBLIGATORIO', max_length=50),
        ),
    ]
