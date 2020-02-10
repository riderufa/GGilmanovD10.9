# Generated by Django 3.0.2 on 2020-02-02 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carslist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carmodel',
            name='producer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='carmodels', to='carslist.Producer'),
        ),
    ]
