# Generated by Django 3.2 on 2021-04-23 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0012_fornecedor_telefone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='cnpj',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nome',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
