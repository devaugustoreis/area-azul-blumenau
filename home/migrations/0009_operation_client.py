# Generated by Django 3.2.7 on 2021-10-07 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20211007_1600'),
    ]

    operations = [
        migrations.AddField(
            model_name='operation',
            name='client',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.client'),
            preserve_default=False,
        ),
    ]
