# Generated by Django 4.2.6 on 2024-05-29 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_rename_uuid_expiration_date_trip_n_uuid_expiration_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trip',
            name='n_uuid_expiration_date',
        ),
        migrations.AddField(
            model_name='trip',
            name='nn_uuid_expiration_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
