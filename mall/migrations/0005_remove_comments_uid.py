# Generated by Django 2.2.7 on 2021-03-09 08:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mall', '0004_auto_20210309_1654'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='uid',
        ),
    ]
