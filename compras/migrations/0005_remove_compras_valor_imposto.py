# Generated by Django 3.1.7 on 2021-03-11 23:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0004_auto_20210311_2014'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compras',
            name='valor_imposto',
        ),
    ]