# Generated by Django 2.2.5 on 2019-10-12 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('userid', models.AutoField(primary_key=True, serialize=False)),
                ('quotes', models.CharField(default=0, max_length=20)),
                ('date', models.CharField(default=0, max_length=20)),
                ('subject', models.CharField(max_length=2000)),
            ],
        ),
    ]