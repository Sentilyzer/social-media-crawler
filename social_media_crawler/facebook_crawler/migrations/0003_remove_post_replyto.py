# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facebook_crawler', '0002_auto_20150324_2317'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='replyto',
        ),
    ]
