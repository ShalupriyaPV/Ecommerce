# Generated by Django 3.2.25 on 2024-07-04 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0010_rename_product_cartitem_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='image',
            field=models.ImageField(default=1, upload_to='images'),
            preserve_default=False,
        ),
    ]
