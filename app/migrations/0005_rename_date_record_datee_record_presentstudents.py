# Generated by Django 4.0.4 on 2022-04-28 05:36

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_record_presentstudents'),
    ]

    operations = [
        migrations.RenameField(
            model_name='record',
            old_name='date',
            new_name='datee',
        ),
        migrations.AddField(
            model_name='record',
            name='presentStudents',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True), blank=True, null=True, size=64),
        ),
    ]