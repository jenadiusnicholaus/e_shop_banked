# Generated by Django 4.2.5 on 2023-10-26 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0006_alter_stockitem_total_estmated_profit_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockitem',
            name='unit_estmated_profit',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]
