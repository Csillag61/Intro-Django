# Generated by Django 2.1.4 on 2018-12-07 02:32

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0009_auto_20181206_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
