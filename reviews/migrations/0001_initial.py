# Generated by Django 3.2 on 2021-04-14 09:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('Email', models.EmailField(max_length=320)),
                ('date', models.DateField(default=datetime.date.today)),
                ('reviews', models.TextField()),
            ],
        ),
    ]
