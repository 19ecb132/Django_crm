# Generated by Django 5.0.6 on 2024-05-24 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='phone',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='record',
            name='pincode',
            field=models.IntegerField(),
        ),
    ]
