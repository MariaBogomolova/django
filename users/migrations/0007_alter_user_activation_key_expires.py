# Generated by Django 4.2 on 2025-02-10 08:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_user_activation_key_expires'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activation_key_expires',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2025, 2, 12, 8, 12, 41, 288903, tzinfo=datetime.timezone.utc), null=True),
        ),
    ]
