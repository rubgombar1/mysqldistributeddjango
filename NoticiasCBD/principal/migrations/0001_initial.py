# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Editorial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=50)),
                ('cuerpo', models.TextField()),
                ('fecha_pub', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
                ('apellidos', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='noticia',
            name='publicador',
            field=models.ForeignKey(to='principal.Persona'),
        ),
        migrations.AddField(
            model_name='editorial',
            name='empleados',
            field=models.ManyToManyField(to='principal.Persona'),
        ),
    ]
