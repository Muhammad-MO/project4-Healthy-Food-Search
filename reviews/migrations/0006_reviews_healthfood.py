# Generated by Django 3.2 on 2021-04-24 23:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('healthfood', '0013_auto_20210423_0548'),
        ('reviews', '0005_alter_reviews_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='healthfood',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='healthfood.healthfood'),
            preserve_default=False,
        ),
    ]
