# Generated by Django 4.2.18 on 2025-03-20 13:56

from django.db import migrations, models
import posts.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0017_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='posts/blank.jpg', upload_to=posts.models.get_upload_path),
        ),
    ]
