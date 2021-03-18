# Generated by Django 3.1.6 on 2021-02-25 09:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about_me', '0005_auto_20210223_1134'),
    ]

    operations = [
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('text', models.TextField()),
            ],
            options={
                'verbose_name': 'Message',
                'verbose_name_plural': 'Messages',
            },
        ),
        migrations.AlterField(
            model_name='news',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 25, 12, 41, 1, 310534)),
        ),
    ]
