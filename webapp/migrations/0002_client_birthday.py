# Generated by Django 5.0.4 on 2024-04-16 09:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='birthday',
            field=models.DateField(default=datetime.datetime(2024, 4, 16, 9, 29, 36, 230889, tzinfo=datetime.timezone.utc), max_length=100),
            preserve_default=False,
        ),
    ]
