# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('query', '0002_auto_20150415_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='author',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='package',
            name='pic1',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='package',
            name='pic2',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='package',
            name='pic3',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='package',
            name='pic4',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='package',
            name='version',
            field=models.CharField(max_length=50, blank=True),
        ),
    ]
