# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-31 20:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0010_change_on_delete_behaviour'),
        ('conversations', '0003_auto_20160131_1915'),
    ]

    operations = [
        migrations.AddField(
            model_name='conversationspage',
            name='main_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
    ]
