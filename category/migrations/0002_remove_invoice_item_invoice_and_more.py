# Generated by Django 4.2.5 on 2023-10-26 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice_item',
            name='invoice',
        ),
        migrations.RemoveField(
            model_name='invoice_item',
            name='product',
        ),
        migrations.RemoveField(
            model_name='invoice_item',
            name='stock',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='product',
        ),
        migrations.DeleteModel(
            name='Invoice',
        ),
        migrations.DeleteModel(
            name='Invoice_Item',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='Stock',
        ),
    ]
