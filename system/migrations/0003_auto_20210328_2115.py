# Generated by Django 2.2.7 on 2021-03-28 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0002_imagefile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='start_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='生效开始时间'),
        ),
        migrations.AlterModelTable(
            name='imagefile',
            table='system_images',
        ),
    ]
