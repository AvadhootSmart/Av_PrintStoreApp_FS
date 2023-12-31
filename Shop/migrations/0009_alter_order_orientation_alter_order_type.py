# Generated by Django 4.2.6 on 2023-11-18 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0008_alter_order_orientation_alter_order_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='orientation',
            field=models.CharField(choices=[('Single', 'Single Page'), ('Double', 'Double Page')], default='SP', max_length=10),
        ),
        migrations.AlterField(
            model_name='order',
            name='type',
            field=models.CharField(choices=[('B&W', 'Black and White'), ('Color', 'Color')], default='B&W', max_length=10),
        ),
    ]
