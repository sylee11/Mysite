# Generated by Django 2.1.12 on 2019-10-10 09:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0002_remove_myuser_date_of_birth'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='catt',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='myuser',
            name='date_of_birth',
            field=models.DateField(default=123),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='myuser',
            name='is_catt',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='myuser',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
    ]
