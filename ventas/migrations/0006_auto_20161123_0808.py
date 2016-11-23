# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0005_auto_20161114_0933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalleventa',
            name='cantidadvendida',
            field=models.IntegerField(default=1),
        ),
    ]
