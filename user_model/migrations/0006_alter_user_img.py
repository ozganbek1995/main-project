# Generated by Django 4.0.1 on 2022-07-12 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_model', '0005_user_email_user_img_user_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='img',
            field=models.ImageField(default='default_user.png', upload_to='profile-img/'),
        ),
    ]