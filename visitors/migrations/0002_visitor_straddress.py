# Generated by Django 3.0.5 on 2021-01-27 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitor',
            name='strAddress',
            field=models.TextField(default='Indonesia'),
        ),
    ]
