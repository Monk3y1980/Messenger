# Generated by Django 3.2.6 on 2021-08-30 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='static/chat/images/default_avatar.png', upload_to='static/chat/images/', verbose_name='Аватар'),
        ),
    ]
