# Generated by Django 4.1.5 on 2023-01-29 23:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_vid_zavedenie_obrazovanie'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rodstvenniki',
            old_name='patronomyc',
            new_name='patronomyc_rod',
        ),
    ]