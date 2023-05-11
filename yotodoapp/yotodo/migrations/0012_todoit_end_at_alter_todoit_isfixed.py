# Generated by Django 4.2 on 2023-05-11 17:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('yotodo', '0011_alter_todoit_isfixed_alter_todoit_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoit',
            name='end_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='todoit',
            name='isfixed',
            field=models.BooleanField(),
        ),
    ]
