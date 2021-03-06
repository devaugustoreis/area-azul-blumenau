# Generated by Django 3.2.7 on 2021-09-27 04:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zip_code', models.CharField(max_length=8)),
                ('state', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
                ('street_name', models.CharField(max_length=100)),
                ('house_number', models.CharField(max_length=6)),
                ('complement', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone1', models.CharField(max_length=20)),
                ('phone2', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.CharField(max_length=100)),
                ('credits', models.FloatField(default=0)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.address')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license_plate', models.CharField(max_length=7)),
                ('entry_time', models.DateTimeField(blank=True, null=True)),
                ('timer', models.IntegerField(blank=True, default=0, null=True)),
                ('vehicle_type', models.CharField(choices=[('C', 'Car'), ('M', 'Moto'), ('O', 'Other')], max_length=1)),
                ('owners', models.ManyToManyField(to='home.Client')),
            ],
        ),
    ]
