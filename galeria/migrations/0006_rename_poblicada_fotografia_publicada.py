# Generated by Django 4.1 on 2024-10-25 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0005_fotografia_poblicada'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fotografia',
            old_name='poblicada',
            new_name='publicada',
        ),
    ]