# Generated by Django 2.1.4 on 2018-12-08 20:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0003_auto_20181207_1255'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personalnote',
            name='isd',
        ),
        migrations.AlterField(
            model_name='personalnote',
            name='note_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='users_app.Note'),
        ),
    ]