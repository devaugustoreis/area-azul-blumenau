# Generated by Django 3.2.7 on 2021-10-11 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_merge_0011_auto_20211009_1442_0011_auto_20211009_1512'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='expiration_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
