# Generated by Django 4.2.18 on 2025-03-03 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_alter_blog_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
