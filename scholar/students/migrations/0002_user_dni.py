# Generated by Django 4.2.6 on 2023-10-28 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='dni',
            field=models.CharField(default='', max_length=10),
        ),
    ]
