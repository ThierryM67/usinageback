# Generated by Django 5.1.2 on 2024-10-29 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manufacturer', '0002_alter_offer_accepted_by_client'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='client',
        ),
        migrations.AddField(
            model_name='rating',
            name='client_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
