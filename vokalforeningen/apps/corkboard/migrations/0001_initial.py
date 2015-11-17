# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40)),
            ],
            options={
                'verbose_name': 'kategori',
                'verbose_name_plural': 'kategorier',
            },
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=60, verbose_name='Titel')),
                ('body', models.TextField(verbose_name='Br\xf8dtekst')),
                ('html', models.TextField(editable=False)),
                ('pub_date', models.DateTimeField(default=datetime.datetime.now)),
                ('mod_date', models.DateTimeField(default=datetime.datetime.now, editable=False)),
                ('is_event', models.BooleanField(default=False, editable=False)),
                ('start', models.DateTimeField(null=True, blank=True)),
                ('end', models.DateTimeField(null=True, verbose_name=b'Slut', blank=True)),
                ('location', models.CharField(max_length=255, verbose_name=b'Sted', blank=True)),
                ('facebook', models.URLField(verbose_name=b'Facebook link', blank=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(blank=True, to='corkboard.Category', null=True)),
            ],
            options={
                'get_latest_by': 'pub_date',
                'verbose_name': 'note',
                'verbose_name_plural': 'noter',
            },
        ),
    ]
