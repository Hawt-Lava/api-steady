# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('steady', '0006_auto_20160311_1343'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prompt',
            name='entry',
        ),
        migrations.RemoveField(
            model_name='scoresheet',
            name='entries',
        ),
        migrations.AddField(
            model_name='entry',
            name='prompt',
            field=models.ForeignKey(default=1, to='steady.Prompt'),
            preserve_default=False,
        ),
    ]
