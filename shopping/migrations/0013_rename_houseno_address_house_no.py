# Generated by Django 3.2.25 on 2024-07-10 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0012_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='houseno',
            new_name='house_no',
        ),
    ]
