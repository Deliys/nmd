# Generated by Django 5.0.6 on 2024-06-14 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_dissertation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dissertation',
            name='author',
        ),
        migrations.AddField(
            model_name='dissertation',
            name='author',
            field=models.ManyToManyField(to='main.autor'),
        ),
    ]
