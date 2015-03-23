# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social_media_crawler', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='comments',
            new_name='replyto',
        ),
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='shares',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
