# Generated by Django 4.2.1 on 2023-05-14 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_elisa_pcr_remove_order_assays_order_assays'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='quantity',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]