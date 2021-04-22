# Generated by Django 3.2 on 2021-04-22 04:44

from django.db import migrations, models
import django.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('healthfood', '0007_alter_healthfood_manufacturer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='healthfood',
            name='manufacturer',
            field=models.ForeignKey(on_delete=django.db.models.fields.CharField, to='healthfood.manufacturer'),
        ),
    ]
