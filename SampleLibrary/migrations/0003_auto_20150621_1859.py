# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('SampleLibrary', '0002_auto_20150610_1627'),
    ]

    operations = [
        migrations.CreateModel(
            name='UnvalidatedSample',
            fields=[
                ('SampleId', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('Organism', models.CharField(max_length=200)),
                ('Tissue', models.CharField(max_length=200)),
                ('ExperimentName', models.CharField(max_length=200)),
                ('DataType', models.CharField(max_length=50)),
                ('GenomeVersion', models.CharField(max_length=100)),
                ('ExperimentDescription', models.CharField(max_length=500)),
                ('isSingleCell', models.BooleanField(default=False)),
                ('isPublishedData', models.BooleanField(default=False)),
                ('Date', models.DateField(null=True)),
                ('Batch', models.CharField(max_length=50)),
                ('SequencingTech', models.CharField(max_length=200)),
                ('RawFileLoc', models.CharField(max_length=200)),
                ('SpecificRawFileLoc', models.CharField(max_length=200)),
                ('LocalBackupLoc', models.CharField(max_length=200)),
                ('RemoteBackupLoc', models.CharField(max_length=200)),
                ('ProcessedFileLoc', models.CharField(max_length=200)),
                ('ConditionCode', models.IntegerField(null=True)),
                ('TimeCode', models.IntegerField(null=True)),
                ('BatchCode', models.IntegerField(null=True)),
                ('IdCode', models.IntegerField(null=True)),
                ('ControlId', models.IntegerField(null=True)),
                ('PreprocessDate', models.DateField(null=True)),
                ('Comments', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='UnvalidatedUpload',
            fields=[
                ('UploadedBy', models.CharField(max_length=100)),
                ('UploadDate', models.DateTimeField(auto_now_add=True)),
                ('UploadId', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
            ],
        ),
        migrations.AddField(
            model_name='unvalidatedsample',
            name='UploadBatch',
            field=models.ForeignKey(default='5d11ad23-940c-4399-ac66-5bb978834b01', to='SampleLibrary.UnvalidatedUpload'),
            preserve_default=False,
        ),
    ]
