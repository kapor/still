# Generated by Django 4.2.18 on 2025-02-10 21:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_post_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='tags',
        ),
    ]
