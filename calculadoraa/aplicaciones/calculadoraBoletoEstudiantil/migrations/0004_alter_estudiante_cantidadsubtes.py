# Generated by Django 5.0.3 on 2024-03-08 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculadoraBoletoEstudiantil', '0003_alter_estudiante_cantidadtrenes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='cantidadSubtes',
            field=models.IntegerField(default=0),
        ),
    ]
