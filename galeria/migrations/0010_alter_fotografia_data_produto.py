# Generated by Django 4.1 on 2024-10-25 20:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0009_alter_fotografia_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fotografia',
            name='data_produto',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
