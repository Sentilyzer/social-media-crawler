# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facebook_crawler', '0003_remove_post_replyto'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='replyto',
            field=models.ForeignKey(to='facebook_crawler.Post', null=True),
            preserve_default=True,
        ),
    ]
