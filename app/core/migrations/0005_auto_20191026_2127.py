# Generated by Django 2.2.5 on 2019-10-26 21:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_recipe'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Recipe',
            new_name='Post',
        ),
    ]
