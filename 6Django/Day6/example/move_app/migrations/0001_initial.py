# Generated by Django 4.2 on 2023-04-19 06:33

import django.core.validators
from django.db import migrations, models
import move_app.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Move',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, validators=[move_app.validators.validate_move_name])),
                ('accuracy', models.PositiveIntegerField(default=70, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
                ('maxPP', models.IntegerField(default=20, validators=[django.core.validators.MinValueValidator(5), django.core.validators.MaxValueValidator(30)])),
                ('pp', models.IntegerField(default=20, validators=[django.core.validators.MinValueValidator(1)])),
                ('power', models.PositiveIntegerField(default=80, validators=[django.core.validators.MaxValueValidator(120)])),
            ],
        ),
    ]
