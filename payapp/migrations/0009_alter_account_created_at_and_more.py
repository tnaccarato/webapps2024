# Generated by Django 5.0.2 on 2024-04-15 16:07

import payapp.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payapp', '0008_alter_notification_notification_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='created_at',
            field=payapp.models.ThriftTimestampField(),
        ),
        migrations.AlterField(
            model_name='notification',
            name='created_at',
            field=payapp.models.ThriftTimestampField(),
        ),
        migrations.AlterField(
            model_name='request',
            name='created_at',
            field=payapp.models.ThriftTimestampField(),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='created_at',
            field=payapp.models.ThriftTimestampField(),
        ),
    ]
