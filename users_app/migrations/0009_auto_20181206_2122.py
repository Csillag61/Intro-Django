# Generated by Django 2.1.4 on 2018-12-07 02:22

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0008_auto_20181206_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]