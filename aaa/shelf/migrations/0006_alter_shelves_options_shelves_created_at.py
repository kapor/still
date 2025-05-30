# Generated by Django 4.2.18 on 2025-03-20 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shelf', '0005_alter_shelves_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shelves',
            options={'ordering': ['-created_at'], 'verbose_name_plural': 'Shelves'},
        ),
        migrations.AddField(
            model_name='shelves',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
