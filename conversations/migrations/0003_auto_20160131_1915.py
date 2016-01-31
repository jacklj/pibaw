# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-31 19:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailredirects', '0005_capitalizeverbose'),
        ('wagtailcore', '0023_alter_page_revision_on_delete_behaviour'),
        ('wagtailforms', '0003_capitalizeverbose'),
        ('conversations', '0002_remove_conversationpage_conversation_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConversationsPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('page_title', models.CharField(max_length=255)),
                ('intro', wagtail.wagtailcore.fields.RichTextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.RemoveField(
            model_name='allconversationspage',
            name='page_ptr',
        ),
        migrations.DeleteModel(
            name='AllConversationsPage',
        ),
    ]
