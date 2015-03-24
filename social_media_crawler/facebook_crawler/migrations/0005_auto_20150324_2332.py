# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facebook_crawler', '0004_post_replyto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='replyto',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
