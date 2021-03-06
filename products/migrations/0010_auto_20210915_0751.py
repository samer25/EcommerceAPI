# Generated by Django 3.2.7 on 2021-09-15 07:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20210912_1305'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='discount_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='date_added',
            field=models.DateTimeField(verbose_name=datetime.datetime(2021, 9, 15, 7, 51, 44, 1799, tzinfo=utc)),
        ),
    ]
