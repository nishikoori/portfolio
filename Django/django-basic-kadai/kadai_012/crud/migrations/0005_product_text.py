# Generated by Django 5.0.6 on 2024-07-01 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0004_product_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
    ]
