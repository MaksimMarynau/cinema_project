# Generated by Django 3.1.4 on 2020-12-16 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='ip',
            field=models.CharField(default='', max_length=15, verbose_name='IP adress'),
        ),
    ]
