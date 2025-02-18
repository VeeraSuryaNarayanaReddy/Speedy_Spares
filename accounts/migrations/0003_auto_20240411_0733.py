# Generated by Django 3.2.20 on 2024-04-11 07:33

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20240411_0731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('120c1d55-586b-44bf-a33b-7ed10131d40f'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
