# Generated by Django 3.2.6 on 2021-08-21 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_auto_20210821_1540'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ('date',), 'verbose_name': 'Сообщение', 'verbose_name_plural': 'Сообщения'},
        ),
    ]
