# Generated by Django 5.0.6 on 2024-07-26 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionPedidos', '0007_pedidos_nombre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedidos',
            name='numero',
        ),
        migrations.AddField(
            model_name='pedidos',
            name='enProceso',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pedidos',
            name='verificando',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
