# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budgetlog',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 19, 12, 34, 39, 463053, tzinfo=utc)),
        ),
    ]
