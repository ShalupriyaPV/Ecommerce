# Generated by Django 3.2.25 on 2024-07-10 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0013_rename_houseno_address_house_no'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='house_no',
            new_name='House_no',
        ),
    ]
