# Generated by Django 2.1.12 on 2019-10-10 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0004_remove_myuser_date_of_birth'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='is_catt',
        ),
    ]
