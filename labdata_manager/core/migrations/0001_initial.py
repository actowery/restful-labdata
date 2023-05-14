# Generated by Django 4.2.1 on 2023-05-12 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0003_rename_is_admin_employee_is_supervisor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='accounts.customuser')),
            ],
        ),
    ]
