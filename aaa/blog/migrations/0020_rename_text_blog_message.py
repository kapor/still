# Generated by Django 4.2.18 on 2025-03-05 17:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_rename_create_date_blog_created_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='text',
            new_name='message',
        ),
    ]
