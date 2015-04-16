# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('query', '0003_auto_20150415_1542'),
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('picture_url', models.URLField()),
                ('picture_description', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='package',
            name='pic1',
        ),
        migrations.RemoveField(
            model_name='package',
            name='pic2',
        ),
        migrations.RemoveField(
            model_name='package',
            name='pic3',
        ),
        migrations.RemoveField(
            model_name='package',
            name='pic4',
        ),
        migrations.AddField(
            model_name='picture',
            name='package',
            field=models.ForeignKey(to='query.Package'),
        ),
    ]
