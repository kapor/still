# Generated by Django 4.2.18 on 2025-02-11 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0003_alter_group_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='description_html',
            field=models.TextField(blank=True, default='No description yet.', editable=False),
        ),
    ]
