# Generated by Django 3.1.4 on 2021-07-06 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tickets',
            fields=[
                ('ticket_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('title', models.TextField()),
                ('summary', models.CharField(max_length=100)),
            ],
        ),
    ]
