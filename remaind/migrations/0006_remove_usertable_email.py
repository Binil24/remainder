# Generated by Django 2.2.5 on 2019-10-13 05:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('remaind', '0005_remaindtbl_loginuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usertable',
            name='email',
        ),
    ]