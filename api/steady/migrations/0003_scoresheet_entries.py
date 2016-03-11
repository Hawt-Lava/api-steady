# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('steady', '0002_auto_20160311_1700'),
    ]

    operations = [
        migrations.AddField(
            model_name='scoresheet',
            name='entries',
            field=models.ForeignKey(default=[1], to='steady.Entry'),
        ),
    ]
