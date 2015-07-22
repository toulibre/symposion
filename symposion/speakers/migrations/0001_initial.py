# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import markitup.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='As you would like it to appear in the conference program.', max_length=100, verbose_name='Name')),
                ('biography', markitup.fields.MarkupField(help_text="A little bit about you.  Edit using <a href='http://warpedvisions.org/projects/markdown-cheat-sheet/target='_blank'>Markdown</a>.", no_rendered_field=True, verbose_name='Biography', blank=True)),
                ('organisation', models.CharField(max_length=100, blank=True)),
                ('city', models.CharField(max_length=255, verbose_name='City', blank=True)),
                ('need_travel', models.BooleanField(default=False, verbose_name='Need travel?')),
                ('need_hosting', models.BooleanField(default=False, verbose_name='Need hosting?')),
                ('photo', models.ImageField(upload_to=b'speaker_photos', blank=True)),
                ('annotation', models.TextField(blank=True)),
                ('invite_email', models.CharField(max_length=200, unique=True, null=True, db_index=True)),
                ('invite_token', models.CharField(max_length=40, db_index=True)),
                ('created', models.DateTimeField(default=datetime.datetime.now, editable=False)),
                ('_biography_rendered', models.TextField(editable=False, blank=True)),
                ('user', models.OneToOneField(related_name='speaker_profile', null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
    ]
