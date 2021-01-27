# Generated by Django 3.0.5 on 2021-01-27 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dtRegistered', models.DateTimeField(auto_now_add=True)),
                ('dtBirth', models.DateField(max_length=8)),
                ('strFullName', models.CharField(max_length=256)),
                ('strGovtIdNo', models.CharField(max_length=16)),
                ('eGender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('X', 'Other')], default='X', max_length=2)),
            ],
            options={
                'ordering': ['dtRegistered'],
            },
        ),
    ]
