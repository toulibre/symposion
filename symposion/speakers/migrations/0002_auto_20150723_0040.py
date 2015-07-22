# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('symposion_speakers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='speaker',
            name='homestay',
            field=models.BooleanField(default=False, verbose_name='Ok for homestay?'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='speaker',
            name='travel_information',
            field=models.TextField(help_text="It's up to us to buy travel tickets in advance, so tell your constraints, your preference, or even the travel reference you would like to take", verbose_name='Travel information', blank=True),
            preserve_default=True,
        ),
    ]
