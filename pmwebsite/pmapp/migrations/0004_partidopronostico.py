# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pmapp', '0003_auto_20150814_0211'),
    ]

    operations = [
        migrations.CreateModel(
            name='PartidoPronostico',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gteam1', models.SmallIntegerField(null=True, blank=True)),
                ('gteam2', models.SmallIntegerField(null=True, blank=True)),
                ('match', models.ForeignKey(to='pmapp.Partido')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
