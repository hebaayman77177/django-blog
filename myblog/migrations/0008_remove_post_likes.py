# Generated by Django 3.2.3 on 2021-05-24 03:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0007_auto_20210524_0231'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
    ]