# Generated by Django 2.2.5 on 2019-10-12 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('remaind', '0004_usertable'),
    ]

    operations = [
        migrations.AddField(
            model_name='remaindtbl',
            name='loginuser',
            field=models.CharField(default=0, max_length=20),
        ),
    ]
