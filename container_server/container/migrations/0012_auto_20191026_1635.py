#  Copyright (C) AI Power - All Rights Reserved
#  Unauthorized copying of this file, via any medium is strictly prohibited
#  Proprietary and confidential
#  Written by AI Power, January 2020

# Generated by Django 2.2.6 on 2019-10-26 09:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('container', '0011_auto_20191026_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camera',
            name='container_side',
            field=models.IntegerField(choices=[(1, 'Front'), (2, 'Back'), (3, 'Left'), (4, 'Right'), (5, 'Above'), (6, 'Beneath')], default=2),
        ),
        migrations.CreateModel(
            name='SingleHandlingWorkerConfig',
            fields=[
                ('config_id', models.AutoField(primary_key=True, serialize=False)),
                ('back_camera', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='back_camera', to='container.Camera')),
                ('front_camera', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='front_camera', to='container.Camera')),
                ('handling', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='container.ContainerHandling')),
                ('left_camera', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='left_camera', to='container.Camera')),
                ('right_camera', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='right_camera', to='container.Camera')),
            ],
        ),
    ]
