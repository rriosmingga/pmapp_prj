# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pmapp', '0002_auto_20150814_0208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partido',
            name='gteam1',
            field=models.SmallIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='partido',
            name='gteam2',
            field=models.SmallIntegerField(null=True, blank=True),
        ),
    ]
