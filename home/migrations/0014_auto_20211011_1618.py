# Generated by Django 3.2.7 on 2021-10-11 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_vehicle_expiration_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='entry_time',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='expiration_time',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
