# Generated by Django 4.0.6 on 2023-10-11 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0003_account_created_on_transaction_created_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='pin',
            field=models.PositiveSmallIntegerField(default=None, null=True),
        ),
    ]
