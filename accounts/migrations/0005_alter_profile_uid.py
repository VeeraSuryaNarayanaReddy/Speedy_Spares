# Generated by Django 3.2.20 on 2024-04-11 07:47

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_profile_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('6617687f-887b-4e2b-8904-88ffcbd2635a'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
