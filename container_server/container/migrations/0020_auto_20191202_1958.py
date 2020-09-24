#  Copyright (C) AI Power - All Rights Reserved
#  Unauthorized copying of this file, via any medium is strictly prohibited
#  Proprietary and confidential
#  Written by AI Power, January 2020

# Generated by Django 2.2.6 on 2019-12-02 12:58

from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('container', '0019_auto_20191202_1942'),
    ]

    operations = [
        migrations.CreateModel(
            name='InOutHistory',
            fields=[
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_datetime', models.DateTimeField(auto_now=True)),
                ('inout', models.IntegerField(choices=[(1, 'In'), (2, 'Out')])),
                ('container_code', models.CharField(max_length=18)),
                ('captured_images', jsonfield.fields.JSONField(default=dict)),
                ('back_camera', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='log_back_camera', to='container.Camera')),
                ('front_camera', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='log_front_camera', to='container.Camera')),
                ('left_camera', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='log_left_camera', to='container.Camera')),
                ('right_camera', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='log_right_camera', to='container.Camera')),
            ],
        ),
        migrations.RenameField(
            model_name='ocrworker',
            old_name='config_id',
            new_name='worker_id',
        ),
        migrations.DeleteModel(
            name='ContainerLog',
        ),
    ]