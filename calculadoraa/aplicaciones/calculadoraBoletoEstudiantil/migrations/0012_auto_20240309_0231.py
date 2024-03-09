# Generated by Django 3.2.12 on 2024-03-09 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculadoraBoletoEstudiantil', '0011_auto_20240309_0219'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiante',
            name='total_bondis_mes',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='estudiante',
            name='total_subtes_mes',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='estudiante',
            name='total_trenes_mes',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
    ]
