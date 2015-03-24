# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facebook_crawler', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='id',
        ),
        migrations.AlterField(
            model_name='post',
            name='graph_id',
            field=models.CharField(max_length=50, serialize=False, primary_key=True),
            preserve_default=True,
        ),
    ]
