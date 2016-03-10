# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('steady', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='foo',
            name='name',
            field=models.TextField(default='Foo Default'),
            preserve_default=False,
        ),
    ]
