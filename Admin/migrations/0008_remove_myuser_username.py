# Generated by Django 2.1.12 on 2019-10-10 09:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0007_auto_20191010_1622'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='username',
        ),
    ]
