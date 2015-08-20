# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pmapp', '0004_partidopronostico'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='partidopronostico',
            unique_together=set([('match', 'user')]),
        ),
    ]
