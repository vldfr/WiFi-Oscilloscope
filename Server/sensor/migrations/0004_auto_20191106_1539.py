# Generated by Django 2.2.6 on 2019-11-06 15:39

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sensor', '0003_sensordata'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sensordata',
            name='sensor',
        ),
        migrations.AlterField(
            model_name='sensordata',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 6, 15, 39, 37, 885830, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='SensorReadingGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(default=datetime.datetime(2019, 11, 6, 15, 39, 37, 885443, tzinfo=utc))),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sensor.Sensor')),
            ],
        ),
        migrations.AddField(
            model_name='sensordata',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sensor.SensorReadingGroup'),
        ),
    ]