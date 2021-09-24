# Generated by Django 3.2.6 on 2021-08-20 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('koderapp', '0002_rename_adress_info_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='InCoding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Ad')),
                ('img', models.ImageField(upload_to='media/', verbose_name='Sekil')),
                ('is_published', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=255, verbose_name='Link')),
                ('name', models.CharField(max_length=255, verbose_name='Ad')),
                ('img', models.ImageField(upload_to='media/', verbose_name='Sekil')),
                ('is_published', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='info',
            name='is_published',
            field=models.BooleanField(default=True),
        ),
    ]