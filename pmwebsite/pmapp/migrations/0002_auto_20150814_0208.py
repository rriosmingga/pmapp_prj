# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pmapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='partido',
            name='date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='partido',
            name='definition',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='partido',
            name='gteam1',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='partido',
            name='gteam2',
            field=models.SmallIntegerField(null=True),
        ),
    ]
