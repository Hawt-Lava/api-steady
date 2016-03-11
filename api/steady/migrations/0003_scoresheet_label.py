# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('steady', '0002_auto_20160311_2024'),
    ]

    operations = [
        migrations.AddField(
            model_name='scoresheet',
            name='label',
            field=models.TextField(default='Default'),
            preserve_default=False,
        ),
    ]
