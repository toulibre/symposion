# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import markitup.fields


class Migration(migrations.Migration):

    dependencies = [
        ('symposion_schedule', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(help_text='Used in case of cancelling', max_length=75, verbose_name='Email')),
                ('name', models.CharField(max_length=100, verbose_name='Your name')),
                ('interests', models.TextField(help_text='Your project', null=True, verbose_name='Interests', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('prerequistes', markitup.fields.MarkupField(help_text='Softwares to be installed, version, etc.', no_rendered_field=True, null=True, verbose_name='Prerequistes', blank=True)),
                ('max_attendees', models.IntegerField(verbose_name='Max attendees')),
                ('_prerequistes_rendered', models.TextField(editable=False, blank=True)),
                ('presentation', models.OneToOneField(related_name='registration', to='symposion_schedule.Presentation')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='attendee',
            name='register_to',
            field=models.ForeignKey(related_name='attendees', to='symposion_registration.Registration'),
            preserve_default=True,
        ),
    ]
