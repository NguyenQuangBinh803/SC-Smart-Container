#  Copyright (C) AI Power - All Rights Reserved
#  Unauthorized copying of this file, via any medium is strictly prohibited
#  Proprietary and confidential
#  Written by AI Power, January 2020

# Generated by Django 2.2.6 on 2019-10-26 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('container', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='camera',
            name='container_side',
            field=models.IntegerField(choices=[(1, 'Front'), (2, 'Behind'), (3, 'Left'), (4, 'Right'), (5, 'Above'), (6, 'Under')], default=2),
        ),
        migrations.AddField(
            model_name='camera',
            name='status',
            field=models.IntegerField(choices=[(1, 'Ready'), (2, 'Disconnected')], default=1),
        ),
        migrations.AlterField(
            model_name='camera',
            name='camera_name',
            field=models.CharField(default='Camera', max_length=45),
        ),
    ]
