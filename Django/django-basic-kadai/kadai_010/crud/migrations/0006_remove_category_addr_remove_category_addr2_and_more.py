# Generated by Django 5.0.6 on 2024-06-26 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0005_category_addr_category_addr2_category_addr3'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='addr',
        ),
        migrations.RemoveField(
            model_name='category',
            name='addr2',
        ),
        migrations.RemoveField(
            model_name='category',
            name='addr3',
        ),
    ]
