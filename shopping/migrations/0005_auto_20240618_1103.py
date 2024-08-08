# Generated by Django 3.2.25 on 2024-06-18 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0004_delete_edit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='img',
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default=1, upload_to='image'),
            preserve_default=False,
        ),
    ]