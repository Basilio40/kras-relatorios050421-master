# Generated by Django 3.1.7 on 2021-03-11 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0004_auto_20210311_1937'),
        ('compras', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compras',
            name='descricao',
            field=models.ManyToManyField(to='cadastro.Compras'),
        ),
    ]
