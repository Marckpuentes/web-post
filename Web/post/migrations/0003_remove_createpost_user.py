# Generated by Django 3.2 on 2021-04-24 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20210422_2144'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='createpost',
            name='user',
        ),
    ]
