# Generated by Django 3.1.4 on 2020-12-10 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0005_auto_20201210_1726'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointmentinstance',
            old_name='apointment',
            new_name='appointment',
        ),
    ]
