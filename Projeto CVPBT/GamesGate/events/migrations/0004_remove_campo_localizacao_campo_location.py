# Generated by Django 4.0.4 on 2023-10-28 00:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_remove_categorie_category_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campo',
            name='localizacao',
        ),
        migrations.AddField(
            model_name='campo',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='events.localizacao'),
        ),
    ]