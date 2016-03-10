# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('steady', '0002_foo_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Foo',
        ),
    ]
