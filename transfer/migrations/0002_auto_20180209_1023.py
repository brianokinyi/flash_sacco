# Generated by Django 2.0.2 on 2018-02-09 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transfer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transfer',
            name='amount',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='userAccNo',
            field=models.IntegerField(),
        ),
    ]
