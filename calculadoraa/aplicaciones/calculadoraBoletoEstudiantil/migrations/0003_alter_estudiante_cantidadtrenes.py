# Generated by Django 5.0.3 on 2024-03-08 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculadoraBoletoEstudiantil', '0002_alter_estudiante_cantidadbondis_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='cantidadTrenes',
            field=models.CharField(max_length=100),
        ),
    ]
