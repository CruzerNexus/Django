# Generated by Django 2.1.7 on 2019-02-27 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GroceryItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_discription', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(verbose_name='date published')),
                ('completed_date', models.DateTimeField(verbose_name='date completed')),
                ('completed_yn', models.BooleanField()),
            ],
        ),
    ]
