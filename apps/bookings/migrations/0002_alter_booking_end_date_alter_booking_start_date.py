# Generated by Django 5.1.1 on 2024-09-14 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='end_date',
            field=models.DateField(verbose_name='end date'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='start_date',
            field=models.DateField(verbose_name='start date'),
        ),
    ]
