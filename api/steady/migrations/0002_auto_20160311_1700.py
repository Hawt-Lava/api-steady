# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('steady', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='prompt',
            field=models.ForeignKey(default=1, to='steady.Prompt'),
        ),
    ]
