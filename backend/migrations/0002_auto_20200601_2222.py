# Generated by Django 3.0.6 on 2020-06-01 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Yonetim_User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yonetim_name', models.CharField(blank=True, max_length=1000, null=True)),
                ('yonetim_password', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='User',
            new_name='Users',
        ),
    ]
