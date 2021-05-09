# Generated by Django 3.1.7 on 2021-03-11 23:09

import computed_property.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0002_auto_20210311_1955'),
    ]

    operations = [
        migrations.AddField(
            model_name='compras',
            name='imposto',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='compras',
            name='porcentagem_impostos',
            field=models.DecimalField(decimal_places=10, default=0.0, max_digits=50),
        ),
        migrations.AddField(
            model_name='compras',
            name='valor',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=50),
        ),
        migrations.AddField(
            model_name='compras',
            name='valor_imposto',
            field=computed_property.fields.ComputedFloatField(compute_from='calcular_imposto', default=0, editable=False),
            preserve_default=False,
        ),
    ]