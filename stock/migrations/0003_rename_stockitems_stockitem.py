# Generated by Django 4.2.5 on 2023-10-26 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_code_alter_product_name'),
        ('stock', '0002_rename_type_stock_status_remove_stock_product_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='StockItems',
            new_name='StockItem',
        ),
    ]