# Generated by Django 4.2.6 on 2024-06-04 17:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0021_sharedtrip_archivedtrips_trip_archivedtrips'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sharedtrip',
            name='archivedTrips',
        ),
        migrations.RemoveField(
            model_name='trip',
            name='archivedTrips',
        ),
        migrations.CreateModel(
            name='archivedTrips',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trips', models.JSONField(blank=True, default=list)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]