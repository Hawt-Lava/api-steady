# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('steady', '0004_auto_20160310_2337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='prompt',
            field=models.ForeignKey(to='steady.Prompt'),
        ),
    ]
