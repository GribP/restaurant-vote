# Generated by Django 4.2.1 on 2023-05-20 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0001_initial'),
        ('menus', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='menus',
            unique_together={('restaurant', 'date')},
        ),
    ]
