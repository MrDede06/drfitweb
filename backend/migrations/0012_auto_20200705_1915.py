# Generated by Django 3.0.6 on 2020-07-05 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0011_remove_dietprogramlist_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programlist',
            name='replycount',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='programlist',
            name='resttime',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='programlist',
            name='setcount',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
