# Generated by Django 3.1.4 on 2020-12-10 16:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0003_auto_20201210_1716'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointmentinstance',
            name='appointment',
        ),
        migrations.AddField(
            model_name='createappointment',
            name='status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='record.createappointment'),
        ),
    ]
