# Generated by Django 4.2.6 on 2023-11-28 20:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0015_sales_alter_order_costtopay'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='CostToPay',
        ),
    ]