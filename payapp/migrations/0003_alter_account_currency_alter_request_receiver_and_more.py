# Generated by Django 5.0.2 on 2024-03-07 01:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payapp', '0002_alter_account_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='currency',
            field=models.CharField(choices=[('gbp', 'GBP'), ('usd', 'USD'), ('eur', 'EUR')], default='gbp', max_length=3),
        ),
        migrations.AlterField(
            model_name='request',
            name='receiver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='request_receiver', to='payapp.account'),
        ),
        migrations.AlterField(
            model_name='request',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='request_sender', to='payapp.account'),
        ),
        migrations.AlterField(
            model_name='request',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('declined', 'Declined'), ('cancelled', 'Cancelled')], default='pending', max_length=10),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='receiver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transaction_receiver', to='payapp.account'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transaction_sender', to='payapp.account'),
        ),
    ]
