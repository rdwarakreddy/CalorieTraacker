# Generated by Django 4.2.1 on 2023-05-26 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_orders_totalcost_alter_orders_totalquantity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='discount_price',
            new_name='Carbohydrates',
        ),
        migrations.AddField(
            model_name='products',
            name='Minerals',
            field=models.FloatField(default='1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='products',
            name='Proteins',
            field=models.FloatField(default='1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='products',
            name='fats',
            field=models.FloatField(default='1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='products',
            name='vitamins',
            field=models.FloatField(default='1'),
            preserve_default=False,
        ),
    ]