# Generated by Django 4.0.2 on 2022-02-14 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Falcon9Launches', '0006_alter_launchcomplex_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='launchcomplex',
            name='image',
        ),
    ]
