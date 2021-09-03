# Generated by Django 3.2.6 on 2021-09-03 16:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='working_days_off',
            field=models.PositiveIntegerField(default=0, help_text='pick how many working days you home office request covers', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(8)]),
        ),
    ]
