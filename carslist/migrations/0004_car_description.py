# Generated by Django 3.0.2 on 2020-02-04 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carslist', '0003_car_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
