# Generated by Django 4.2.18 on 2025-02-19 14:44

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_delete_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, default='images/blank.jpg', upload_to=blog.models.get_upload_path, verbose_name='Uploaded Image'),
        ),
    ]
