# Generated by Django 4.2.4 on 2023-08-14 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='due',
            field=models.DateField(null=True),
        ),
    ]
