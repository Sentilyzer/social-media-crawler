# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField()),
                ('name', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('likes', models.IntegerField()),
                ('shares', models.IntegerField()),
                ('comments', models.ForeignKey(to='social_media_crawler.Post', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
