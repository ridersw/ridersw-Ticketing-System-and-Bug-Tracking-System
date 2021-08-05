# Generated by Django 3.1.4 on 2021-07-11 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0004_tickets_assigned_engineer'),
    ]

    operations = [
        migrations.AddField(
            model_name='tickets',
            name='focused',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tickets',
            name='status',
            field=models.CharField(choices=[('Open', 'Open'), ('In Progress', 'In Progress'), ('Pending', 'Pending'), ('On Hold', 'On Hold'), ('Closed', 'Closed')], default='Open', max_length=20),
        ),
    ]