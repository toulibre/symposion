# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('symposion_registration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendee',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Your name or pseudo'),
            preserve_default=True,
        ),
    ]
