# Generated by Django 4.2 on 2023-05-03 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yotodo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todoit',
            options={'verbose_name': 'Задачи пользователей', 'verbose_name_plural': 'Задачи пользователей'},
        ),
        migrations.AlterField(
            model_name='todoit',
            name='user',
            field=models.CharField(max_length=20),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
