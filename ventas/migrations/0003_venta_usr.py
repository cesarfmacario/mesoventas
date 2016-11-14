# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0002_auto_20161114_0929'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='usr',
            field=models.CharField(max_length=25, default=''),
        ),
    ]
