# Generated by Django 4.2.2 on 2023-08-04 17:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0010_remove_appointment_online_time_slot_online_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_profile',
            name='order',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='time_appointment_create',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 4, 17, 38, 46, 818290)),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='token',
            field=models.CharField(default='0Z91soE179Eu4htxY0EgQ21A4CCrm313TRM7sWMfsWQ', max_length=200),
        ),
    ]
