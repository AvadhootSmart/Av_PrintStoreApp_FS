# Generated by Django 4.2.6 on 2023-11-18 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0010_alter_order_orientation_alter_order_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='type',
            new_name='ColorType',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='file',
            new_name='UploadFile',
        ),
        migrations.AlterField(
            model_name='order',
            name='orientation',
            field=models.CharField(choices=[('Single', 'Single Page'), ('Double', 'Double Page')], max_length=50),
        ),
    ]
