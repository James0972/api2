# Generated by Django 4.2.6 on 2024-02-27 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='account_balance',
            field=models.PositiveIntegerField(default=100),
        ),
    ]