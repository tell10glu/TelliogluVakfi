# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Haber',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('baslik', models.CharField(max_length=50)),
                ('onyazi', models.CharField(max_length=150)),
                ('anayazi', models.TextField()),
                ('resim1', models.CharField(max_length=200)),
                ('resim2', models.CharField(max_length=200)),
                ('resim3', models.CharField(max_length=200)),
                ('resim4', models.CharField(max_length=200)),
                ('resim5', models.CharField(max_length=200)),
                ('resim6', models.CharField(max_length=200)),
                ('vidyo_url', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='HaberKategori',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('kategori_adi', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='haber',
            name='kategori',
            field=models.ForeignKey(to='yonetim.HaberKategori'),
        ),
    ]
