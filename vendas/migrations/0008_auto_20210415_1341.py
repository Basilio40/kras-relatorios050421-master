# Generated by Django 3.1.7 on 2021-04-15 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0007_auto_20210415_1338'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servicovenda',
            old_name='cliente',
            new_name='venda',
        ),
    ]
