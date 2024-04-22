# Generated by Django 5.0.4 on 2024-04-21 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Codigoproduto', models.CharField(max_length=20)),
                ('Nome', models.EmailField(max_length=40)),
                ('Codigobarras', models.CharField(max_length=20)),
                ('Preço', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'tblemployee',
            },
        ),
    ]
