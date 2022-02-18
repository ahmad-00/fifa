# Generated by Django 4.0.2 on 2022-02-18 14:15

import django.contrib.postgres.indexes
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_player_position_category_and_more'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='player',
            name='player_positio_9bde1f_hash',
        ),
        migrations.AddIndex(
            model_name='player',
            index=django.contrib.postgres.indexes.HashIndex(fields=['position_category'], name='player_positio_41d62d_hash'),
        ),
    ]
