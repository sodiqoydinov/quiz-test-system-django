# Generated by Django 3.0.5 on 2023-02-11 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0005_auto_20201209_2125'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='n_marta',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
