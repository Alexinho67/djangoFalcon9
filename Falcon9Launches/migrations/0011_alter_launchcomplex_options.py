# Generated by Django 4.0.2 on 2022-02-16 19:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Falcon9Launches', '0010_remove_flight_launch_site_flight_launch_complex'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='launchcomplex',
            options={'verbose_name_plural': 'Launch complexes'},
        ),
    ]