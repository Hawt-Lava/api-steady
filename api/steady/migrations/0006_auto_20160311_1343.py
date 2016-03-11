# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('steady', '0005_auto_20160311_1314'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='prompt',
        ),
        migrations.AddField(
            model_name='prompt',
            name='entry',
            field=models.ForeignKey(related_name='prompt', default='', to='steady.Entry'),
            preserve_default=False,
        ),
    ]
