# Generated by Django 3.2.25 on 2024-06-11 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='img',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]