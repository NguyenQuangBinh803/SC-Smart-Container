#  Copyright (C) AI Power - All Rights Reserved
#  Unauthorized copying of this file, via any medium is strictly prohibited
#  Proprietary and confidential
#  Written by AI Power, January 2020

# Generated by Django 2.2.6 on 2019-10-26 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Camera',
            fields=[
                ('camera_id', models.AutoField(primary_key=True, serialize=False)),
                ('camera_name', models.TextField(default='Camera', max_length=45)),
                ('stream_url', models.URLField(default='')),
            ],
        ),
    ]