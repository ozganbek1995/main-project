# Generated by Django 4.0.4 on 2022-07-21 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_report'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='activ',
            field=models.BooleanField(default=False),
        ),
    ]