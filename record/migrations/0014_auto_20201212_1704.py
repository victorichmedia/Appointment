# Generated by Django 3.1.4 on 2020-12-12 16:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0013_auto_20201212_1659'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='createappointment',
            name='status',
        ),
        migrations.AlterField(
            model_name='appointmentinstance',
            name='appointment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='record.createappointment'),
        ),
    ]