# Generated by Django 3.2.7 on 2021-10-07 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_client_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='profile_pic',
            field=models.ImageField(blank=True, default='generic_profile.png', null=True, upload_to=''),
        ),
    ]