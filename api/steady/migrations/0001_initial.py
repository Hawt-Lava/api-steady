# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = []

    operations = [
        migrations.CreateModel(name='Entry',
                               fields=[
                                   ('id', models.AutoField(verbose_name='ID',
                                                           serialize=False,
                                                           auto_created=True,
                                                           primary_key=True)),
                                   ('score', models.IntegerField()),
                               ], ),
        migrations.CreateModel(name='Foo',
                               fields=[
                                   ('id', models.AutoField(verbose_name='ID',
                                                           serialize=False,
                                                           auto_created=True,
                                                           primary_key=True)),
                                   ('name', models.TextField()),
                               ], ),
        migrations.CreateModel(name='Prompt',
                               fields=[
                                   ('id', models.AutoField(verbose_name='ID',
                                                           serialize=False,
                                                           auto_created=True,
                                                           primary_key=True)),
                                   ('text', models.TextField()),
                               ], ),
        migrations.CreateModel(
            name='ScoreSheet',
            fields=[
                ('id', models.AutoField(verbose_name='ID',
                                        serialize=False,
                                        auto_created=True,
                                        primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('entries', models.ForeignKey(to='steady.Entry')),
            ], ),
        migrations.AddField(model_name='entry',
                            name='prompt',
                            field=models.ForeignKey(default=1,
                                                    to='steady.Prompt'), ),
    ]
