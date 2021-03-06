# Generated by Django 3.0.2 on 2020-02-02 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Producer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('transmission', models.CharField(choices=[('A', 'automatic'), ('M', 'manual')], max_length=50)),
                ('car_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='carslist.CarModel')),
                ('color', models.ManyToManyField(related_name='cars', to='carslist.Color')),
                ('producer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='carslist.Producer')),
            ],
        ),
    ]
