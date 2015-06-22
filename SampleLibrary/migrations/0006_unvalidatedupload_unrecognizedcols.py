# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SampleLibrary', '0005_auto_20150621_1934'),
    ]

    operations = [
        migrations.AddField(
            model_name='unvalidatedupload',
            name='UnrecognizedCols',
            field=models.CharField(default='', max_length=2000),
            preserve_default=False,
        ),
    ]
