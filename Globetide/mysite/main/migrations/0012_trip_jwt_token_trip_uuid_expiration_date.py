# Generated by Django 4.2.6 on 2024-05-29 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_budgetitem_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='jwt_token',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='trip',
            name='uuid_expiration_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]