# Generated by Django 4.2.18 on 2025-02-16 16:18

from django.db import migrations, models
import shelf.models


class Migration(migrations.Migration):

    dependencies = [
        ('shelf', '0004_delete_shelflist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shelves',
            name='image',
            field=models.ImageField(blank=True, default='shelves/blank.jpg', upload_to=shelf.models.get_upload_path),
        ),
    ]
