# Generated by Django 3.2.7 on 2021-10-07 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_client_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
