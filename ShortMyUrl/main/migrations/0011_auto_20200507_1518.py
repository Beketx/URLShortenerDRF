# Generated by Django 3.0.5 on 2020-05-07 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20200507_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='model_short',
            name='short_url',
            field=models.UUIDField(default=None),
        ),
    ]
