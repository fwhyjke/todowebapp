# Generated by Django 4.2 on 2023-05-08 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yotodo', '0006_alter_todoit_lvl'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoit',
            name='isfixed',
            field=models.IntegerField(default=0),
        ),
    ]