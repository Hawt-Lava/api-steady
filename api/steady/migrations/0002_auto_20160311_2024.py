# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('steady', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scoresheet',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
