# Generated by Django 4.1 on 2024-10-22 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fotografia',
            name='preco',
            field=models.DecimalField(decimal_places=2, default=100.0, max_digits=10),
        ),
    ]