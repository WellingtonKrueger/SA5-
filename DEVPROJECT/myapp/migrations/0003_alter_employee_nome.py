# Generated by Django 4.2.7 on 2024-04-22 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_rename_preço_employee_preco'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='Nome',
            field=models.CharField(max_length=40),
        ),
    ]