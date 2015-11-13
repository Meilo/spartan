# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserLists',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nom', models.CharField(max_length=50, null=True)),
                ('prenom', models.CharField(max_length=50, null=True)),
                ('email', models.EmailField(max_length=100, null=True)),
                ('lists', jsonfield.fields.JSONField(null=True)),
            ],
        ),
    ]
