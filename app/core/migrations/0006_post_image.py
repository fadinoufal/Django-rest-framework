# Generated by Django 2.2.5 on 2019-10-28 18:19

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20191026_2127'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to=core.models.post_image_file_path),
        ),
    ]