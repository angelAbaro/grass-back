# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skyend_configs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contrato',
            name='documentos',
        ),
        migrations.AddField(
            model_name='contrato',
            name='documentos',
            field=models.ForeignKey(blank=True, to='skyend_configs.Documento', null=True),
        ),
    ]
