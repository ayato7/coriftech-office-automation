# Generated by Django 3.2.4 on 2021-11-24 22:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='customuser',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='username',
        ),
    ]
