# Generated by Django 5.1.2 on 2024-11-01 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0007_alter_request_completed_date_alter_request_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='completed_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
