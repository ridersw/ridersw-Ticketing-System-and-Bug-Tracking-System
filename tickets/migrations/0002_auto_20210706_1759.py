# Generated by Django 3.1.4 on 2021-07-06 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tickets',
            name='summary',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='tickets',
            name='title',
            field=models.TextField(max_length=100),
        ),
    ]