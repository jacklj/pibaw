# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-31 19:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conversations', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conversationpage',
            name='conversation_title',
        ),
    ]
