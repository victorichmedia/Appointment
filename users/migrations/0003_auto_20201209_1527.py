# Generated by Django 3.1.4 on 2020-12-09 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_doctor_specification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specification',
            name='name',
            field=models.CharField(help_text='Enter a your specification (e.g. Medical Doctor)', max_length=200),
        ),
    ]