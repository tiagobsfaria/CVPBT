# Generated by Django 4.0.4 on 2023-12-07 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0010_campo_preco_hora'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campo',
            name='image',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]
