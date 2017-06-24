# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('skyend_configs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Archivo',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('foto', models.ImageField(upload_to=b'images/', null=True, verbose_name=b'Imagen')),
            ],
            options={
                'verbose_name': 'Archivo',
                'verbose_name_plural': 'Archivos',
            },
        ),
        migrations.CreateModel(
            name='Cancha',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('precio', models.IntegerField()),
                ('descripcion', models.TextField()),
                ('estado_reserva', models.CharField(default=0, max_length=1, choices=[('0', 'libre'), ('1', 'Reservado'), ('2', 'Ocupado')])),
                ('estado', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Cancha',
                'verbose_name_plural': 'Canchas',
            },
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('razon_social', models.CharField(max_length=100)),
                ('ruc', models.IntegerField()),
                ('logo', models.ImageField(upload_to=b'images/', null=True, verbose_name=b'Imagen')),
                ('descripcion', models.TextField()),
                ('direccion', models.CharField(max_length=100)),
                ('estado', models.BooleanField(default=True)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name': 'Empresa',
                'verbose_name_plural': 'Empresas',
            },
        ),
        migrations.CreateModel(
            name='Local',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('nombre_local', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=100)),
                ('numero_telefono', models.IntegerField(max_length=12)),
                ('estado', models.BooleanField(default=True)),
                ('email', models.EmailField(max_length=254)),
                ('empresa', models.ForeignKey(blank=True, to='skyend_configs.Empresa', null=True)),
            ],
            options={
                'verbose_name': 'Local',
                'verbose_name_plural': 'Locals',
            },
        ),
        migrations.CreateModel(
            name='TipoCancha',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('estado', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'TipoCancha',
                'verbose_name_plural': 'TipoCanchas',
            },
        ),
        migrations.AddField(
            model_name='cancha',
            name='tipo_cancha',
            field=models.ForeignKey(to='skyend_configs.TipoCancha'),
        ),
        migrations.AddField(
            model_name='archivo',
            name='cancha',
            field=models.ForeignKey(to='skyend_configs.Cancha'),
        ),
    ]
