# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0002_userlists_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userlists',
            name='test',
        ),
    ]
