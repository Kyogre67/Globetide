# Generated by Django 4.2.6 on 2024-05-22 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_userprofile_otp_userprofile_otp_expiry_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='additionaldata',
            name='age',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='additionaldata',
            name='sex',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
    ]
