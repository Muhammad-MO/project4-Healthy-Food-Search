# Generated by Django 3.2 on 2021-04-23 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthfood', '0011_auto_20210422_1356'),
    ]

    operations = [
        migrations.RenameField(
            model_name='healthfood',
            old_name='ISBN',
            new_name='country',
        ),
        migrations.AddField(
            model_name='healthfood',
            name='ingredients',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='healthfood',
            name='nutrition',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
    ]