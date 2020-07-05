# Generated by Django 3.0.6 on 2020-07-05 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0009_auto_20200705_1636'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dietprogramlist',
            old_name='afterbfast',
            new_name='ara1',
        ),
        migrations.RenameField(
            model_name='dietprogramlist',
            old_name='afterdinner',
            new_name='ara2',
        ),
        migrations.RenameField(
            model_name='dietprogramlist',
            old_name='afterlunch',
            new_name='ara3',
        ),
        migrations.AddField(
            model_name='dietprogramlist',
            name='ara4',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]