# Generated by Django 3.1.6 on 2021-02-20 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about_me', '0003_auto_20210220_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='result',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
