# Generated by Django 3.2.6 on 2021-08-23 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('koderapp', '0008_remove_incoding_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='BestQuestions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(verbose_name='Sual')),
                ('answer', models.TextField(verbose_name='Cavab')),
                ('is_published', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
