# Generated by Django 5.0.6 on 2024-07-26 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionPedidos', '0005_alter_clientes_nombre_alter_clientes_telefono'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedidos',
            name='comentario',
            field=models.TextField(blank=True, null=True),
        ),
    ]
