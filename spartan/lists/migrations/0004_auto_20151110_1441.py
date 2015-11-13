# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0003_remove_userlists_test'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserLists',
            new_name='UserList',
        ),
    ]
