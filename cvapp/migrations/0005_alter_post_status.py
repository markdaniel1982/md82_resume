# Generated by Django 3.2.19 on 2023-06-01 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cvapp', '0004_auto_20230601_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=1),
        ),
    ]
