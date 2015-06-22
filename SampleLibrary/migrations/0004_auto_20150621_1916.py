# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('SampleLibrary', '0003_auto_20150621_1859'),
        ('auth', '__first__')
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='UploadedBy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
