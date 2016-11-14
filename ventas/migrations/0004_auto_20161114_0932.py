# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0003_venta_usr'),
    ]

    operations = [
        migrations.RenameField(
            model_name='venta',
            old_name='usr',
            new_name='usuario',
        ),
    ]
