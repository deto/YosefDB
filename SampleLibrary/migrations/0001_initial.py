# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('SampleId', models.UUIDField(serialize=False, primary_key=True)),
                ('Organism', models.CharField(max_length=200)),
                ('Tissue', models.CharField(max_length=200)),
                ('ExperimentName', models.CharField(max_length=200)),
                ('DataType', models.CharField(max_length=50)),
                ('GenomeVersion', models.CharField(max_length=100)),
                ('ExperimentDescription', models.CharField(max_length=500)),
                ('isSingleCell', models.BooleanField()),
                ('isPublishedData', models.BooleanField()),
                ('Date', models.DateField()),
                ('Batch', models.CharField(max_length=50)),
                ('SequencingTech', models.CharField(max_length=200)),
                ('RawFileLoc', models.CharField(max_length=200)),
                ('SpecificRawFileLoc', models.CharField(max_length=200)),
                ('LocalBackupLoc', models.CharField(max_length=200)),
                ('RemoteBackupLoc', models.CharField(max_length=200)),
                ('ProcessedFileLoc', models.CharField(max_length=200)),
                ('ConditionCode', models.IntegerField()),
                ('TimeCode', models.IntegerField()),
                ('BatchCode', models.IntegerField()),
                ('IdCode', models.IntegerField()),
                ('ControlId', models.IntegerField()),
                ('PreprocessDate', models.DateField()),
                ('Comments', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('UploadedBy', models.CharField(max_length=100)),
                ('UploadDate', models.DateTimeField(auto_now_add=True)),
                ('UploadId', models.UUIDField(serialize=False, primary_key=True)),
            ],
        ),
        migrations.AddField(
            model_name='sample',
            name='UploadBatch',
            field=models.ForeignKey(to='SampleLibrary.Upload'),
        ),
    ]
