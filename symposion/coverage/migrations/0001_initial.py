# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import symposion.coverage.models


class Migration(migrations.Migration):

    dependencies = [
        ('symposion_schedule', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coverage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, verbose_name='Link text')),
                ('coverage_type', models.CharField(max_length=30, verbose_name='Coverage type', choices=[(b'link', 'Link'), (b'video', 'Video'), (b'audio', 'Audio'), (b'photos', 'Photos'), (b'writeup', 'Write-up'), (b'slides', 'Slides'), (b'transcription', 'Transcription')])),
                ('url', models.URLField(blank=True)),
                ('url2', models.URLField(help_text='Url to another format for audio or video media.', blank=True)),
                ('poster', models.URLField(blank=True)),
                ('coverage_file', models.FileField(upload_to=symposion.coverage.models.generate_filename, verbose_name='Coverage file', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Licence',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('url', models.URLField(verbose_name='Url to licence text')),
            ],
            options={
                'verbose_name': 'Licence',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='coverage',
            name='licence',
            field=models.ForeignKey(verbose_name='Coverage licence', to='symposion_coverage.Licence'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='coverage',
            name='presentation',
            field=models.ForeignKey(related_name='coverages', blank=True, to='symposion_schedule.Presentation', null=True),
            preserve_default=True,
        ),
    ]
