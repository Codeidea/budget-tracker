# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BudgetLog',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateField()),
                ('created_at', models.DateTimeField(default=datetime.datetime(2015, 7, 19, 12, 33, 46, 315049))),
            ],
        ),
        migrations.CreateModel(
            name='LogCategory',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('key', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='budgetlog',
            name='category',
            field=models.ForeignKey(to='tracking.LogCategory', null=True),
        ),
        migrations.AddField(
            model_name='budgetlog',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
