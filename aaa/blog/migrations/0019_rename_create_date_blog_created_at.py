# Generated by Django 4.2.18 on 2025-03-05 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_rename_created_at_blog_create_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='create_date',
            new_name='created_at',
        ),
    ]
