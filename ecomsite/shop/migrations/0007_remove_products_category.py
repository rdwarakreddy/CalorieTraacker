# Generated by Django 4.2.1 on 2023-07-28 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_remove_products_minerals_remove_products_vitamins'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='category',
        ),
    ]
