# Generated by Django 3.2 on 2021-07-07 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Delivery', '0002_auto_20210603_1051'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='status',
            field=models.BooleanField(default=0, null=True),
        ),
    ]
