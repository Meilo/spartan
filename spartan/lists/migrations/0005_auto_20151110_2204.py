# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0004_auto_20151110_1441'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('nom', models.CharField(null=True, max_length=50)),
                ('prenom', models.CharField(null=True, max_length=50)),
                ('email', models.EmailField(null=True, max_length=100)),
                ('mdp', models.CharField(null=True, max_length=100)),
                ('lists', jsonfield.fields.JSONField(null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='UserList',
        ),
    ]
