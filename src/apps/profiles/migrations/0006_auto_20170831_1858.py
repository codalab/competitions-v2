# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-31 18:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_auto_20170829_2009'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='uid',
            new_name='github_uid',
        ),
    ]