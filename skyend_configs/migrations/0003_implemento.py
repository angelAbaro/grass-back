# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('skyend_configs', '0002_auto_20170623_1956'),
    ]

    operations = [
        migrations.CreateModel(
            name='Implemento',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('despcripcion', models.IntegerField()),
                ('logo', models.ImageField(upload_to=b'images/', null=True, verbose_name=b'Imagen')),
                ('estado', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Implemento',
                'verbose_name_plural': 'Implementos',
            },
        ),
    ]
