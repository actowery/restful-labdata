# Generated by Django 4.2.1 on 2023-05-12 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_remove_order_assays_assay_order_assays'),
    ]

    operations = [
        migrations.AddField(
            model_name='assay',
            name='result',
            field=models.CharField(choices=[('P', 'Pass'), ('F', 'Fail'), ('I', 'Incomplete'), ('E', 'Error')], default='I', max_length=1),
        ),
        migrations.AddField(
            model_name='assay',
            name='status',
            field=models.CharField(choices=[('P', 'Pending'), ('R', 'Running'), ('C', 'Complete')], default='P', max_length=1),
        ),
    ]