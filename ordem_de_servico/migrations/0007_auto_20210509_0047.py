# Generated by Django 2.0.13 on 2021-05-09 03:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ordem_de_servico', '0006_auto_20210509_0036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordem',
            name='HT',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='proposta_HT', to='proposta.Proposta'),
        ),
    ]
