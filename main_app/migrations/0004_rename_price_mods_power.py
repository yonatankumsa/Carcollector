# Generated by Django 4.0.6 on 2022-07-20 20:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_mods_car_alter_mods_mod'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mods',
            old_name='price',
            new_name='power',
        ),
    ]
