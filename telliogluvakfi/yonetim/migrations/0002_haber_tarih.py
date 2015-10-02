# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('yonetim', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='haber',
            name='tarih',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 2, 14, 35, 33, 837078, tzinfo=utc), editable=False),
            preserve_default=False,
        ),
    ]
