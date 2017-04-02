# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-21 22:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchingEngine', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='actuator',
            old_name='max_effective_action_force_gt_3',
            new_name='max_effective_action_force_1',
        ),
        migrations.RenameField(
            model_name='actuator',
            old_name='max_effective_action_force_in_1_3',
            new_name='max_effective_action_force_2',
        ),
        migrations.RenameField(
            model_name='actuator',
            old_name='max_effective_action_force_lt_1',
            new_name='max_effective_action_force_3',
        ),
        migrations.AddField(
            model_name='actuator',
            name='max_effective_action_force_border_1',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='actuator',
            name='max_effective_action_force_border_2',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]