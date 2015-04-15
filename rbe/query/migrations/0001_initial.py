# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('program', models.CharField(max_length=300)),
                ('description', models.CharField(max_length=500)),
                ('cover', models.URLField()),
                ('pic1', models.URLField()),
                ('pic2', models.URLField()),
                ('pic3', models.URLField()),
                ('pic4', models.URLField()),
                ('author', models.URLField()),
                ('upstream', models.URLField()),
                ('version', models.CharField(max_length=50)),
            ],
        ),
    ]
