# Generated by Django 4.0.4 on 2023-12-09 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0013_reserva_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='end_time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='start_time',
            field=models.TimeField(),
        ),
    ]
