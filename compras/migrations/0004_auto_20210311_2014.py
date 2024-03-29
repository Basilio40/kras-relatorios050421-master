# Generated by Django 3.1.7 on 2021-03-11 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0003_auto_20210311_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compras',
            name='porcentagem_impostos',
            field=models.DecimalField(decimal_places=4, default=0.0, max_digits=50),
        ),
        migrations.AlterField(
            model_name='compras',
            name='valor_imposto',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=50),
        ),
    ]
