# Generated by Django 3.2.20 on 2024-04-12 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('speedyapp1', '0008_cartitem_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
