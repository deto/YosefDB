# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('SampleLibrary', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sample',
            name='BatchCode',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='ConditionCode',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='ControlId',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='Date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='IdCode',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='PreprocessDate',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='SampleId',
            field=models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='TimeCode',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='isPublishedData',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='sample',
            name='isSingleCell',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='upload',
            name='UploadId',
            field=models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True),
        ),
    ]
