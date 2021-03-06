# Generated by Django 3.1.4 on 2020-12-10 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_doctor_is_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='is_staff',
            field=models.BooleanField(default=True, verbose_name='staff status'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='specification',
            field=models.ManyToManyField(to='users.Specification'),
        ),
    ]
