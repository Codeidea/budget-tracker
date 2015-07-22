# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import timezone_field.fields
import apps.users.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(verbose_name='last login', blank=True, null=True)),
                ('is_superuser', models.BooleanField(verbose_name='superuser status', help_text='Designates that this user has all permissions without explicitly assigning them.', default=False)),
                ('username', models.CharField(blank=True, null=True, max_length=50)),
                ('email', models.EmailField(unique=True, max_length=254)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('timezone', timezone_field.fields.TimeZoneField(default='Europe/Warsaw')),
                ('groups', models.ManyToManyField(verbose_name='groups', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', blank=True, related_query_name='user', to='auth.Group', related_name='user_set')),
                ('user_permissions', models.ManyToManyField(verbose_name='user permissions', help_text='Specific permissions for this user.', blank=True, related_query_name='user', to='auth.Permission', related_name='user_set')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', apps.users.models.UserManager()),
            ],
        ),
    ]
