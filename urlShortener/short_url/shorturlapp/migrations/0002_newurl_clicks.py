# Generated by Django 2.1.7 on 2019-03-05 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shorturlapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newurl',
            name='clicks',
            field=models.IntegerField(default=0),
        ),
    ]
