# Generated by Django 3.2.6 on 2021-08-22 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('koderapp', '0003_auto_20210820_0807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incoding',
            name='img',
            field=models.ImageField(upload_to='static/assets/media/', verbose_name='Sekil'),
        ),
        migrations.AlterField(
            model_name='project',
            name='img',
            field=models.ImageField(upload_to='static/assets/media/', verbose_name='Sekil'),
        ),
    ]
