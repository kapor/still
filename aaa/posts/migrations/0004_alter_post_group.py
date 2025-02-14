# Generated by Django 4.2.18 on 2025-02-11 21:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0004_alter_group_description_html'),
        ('posts', '0003_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='group',
            field=models.OneToOneField(default='None', on_delete=django.db.models.deletion.PROTECT, related_name='posts', to='groups.group'),
        ),
    ]
