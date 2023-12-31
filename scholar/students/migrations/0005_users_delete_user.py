# Generated by Django 4.2.6 on 2023-11-08 00:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_alter_user_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=500)),
                ('status', models.BooleanField(null=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('updated_at', models.DateTimeField(default=datetime.datetime.now)),
                ('deleted_at', models.DateTimeField(default=datetime.datetime.now, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
