# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0005_auto_20151110_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=100, null=True, validators=[django.core.validators.RegexValidator(code='invalid_email', message='Email must be Alphanumeric', regex='^[A-Z0-9._%+-]+@[A-Z0-9.-]+\\.[A-Z]{2,}$')]),
        ),
    ]
