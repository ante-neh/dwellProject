# Generated by Django 5.0 on 2024-01-01 07:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dwellapp', '0002_address_remove_student_city_remove_student_state_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='address',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='dwellapp.address'),
        ),
    ]