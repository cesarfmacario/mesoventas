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
        migrations.AddField(
            model_name='venta',
            name='total',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='detalleventa',
            name='totaldetalle',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='producto',
            name='existencias',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.FloatField(default=0),
        ),
    ]
