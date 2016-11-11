# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='venta',
            old_name='idcliente',
            new_name='cliente',
        ),
    ]
