# Generated by Django 4.1 on 2024-10-25 16:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0006_rename_poblicada_fotografia_publicada'),
    ]

    operations = [
        migrations.AddField(
            model_name='fotografia',
            name='data_fotografia',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
