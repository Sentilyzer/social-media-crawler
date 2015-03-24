# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facebook_crawler', '0005_auto_20150324_2332'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('graph_id', models.CharField(max_length=50, serialize=False, primary_key=True)),
                ('date', models.DateTimeField()),
                ('name', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('likes', models.IntegerField(default=0)),
                ('shares', models.IntegerField(default=0)),
                ('replyto', models.ForeignKey(to='facebook_crawler.Post', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
