# Generated by Django 3.2.20 on 2024-04-13 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('speedyapp1', '0009_cartitem_total_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='total_price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
