# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('skyend_configs', '0003_implemento'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catalogo',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('estado', models.BooleanField(default=True)),
                ('cancha', models.ForeignKey(blank=True, to='skyend_configs.Cancha', null=True)),
                ('implemento', models.ForeignKey(blank=True, to='skyend_configs.Implemento', null=True)),
                ('local', models.ForeignKey(to='skyend_configs.Local')),
            ],
            options={
                'verbose_name': 'Catalogo',
                'verbose_name_plural': 'Catalogos',
            },
        ),
    ]
