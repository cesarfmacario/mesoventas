# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0002_auto_20161111_0932'),
    ]

    operations = [
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
