# Generated by Django 4.2.1 on 2023-05-14 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0006_alter_event_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(verbose_name='Дата'),
        ),
    ]
