# Generated by Django 3.0.6 on 2020-07-05 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0010_auto_20200705_1652'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dietprogramlist',
            name='day',
        ),
    ]
