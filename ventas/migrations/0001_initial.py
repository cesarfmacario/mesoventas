# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('nombre', models.CharField(max_length=100)),
                ('nit', models.CharField(max_length=20)),
                ('direccion', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='DetalleVenta',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('cantidadvendida', models.IntegerField(default=0)),
                ('totaldetalle', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('nombre', models.CharField(max_length=200)),
                ('precio', models.FloatField()),
                ('existencias', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('numfactura', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now)),
                ('idcliente', models.ForeignKey(to='ventas.Cliente')),
                ('productos', models.ManyToManyField(through='ventas.DetalleVenta', to='ventas.Producto')),
            ],
        ),
        migrations.AddField(
            model_name='detalleventa',
            name='producto',
            field=models.ForeignKey(to='ventas.Producto'),
        ),
        migrations.AddField(
            model_name='detalleventa',
            name='venta',
            field=models.ForeignKey(to='ventas.Venta'),
        ),
    ]
