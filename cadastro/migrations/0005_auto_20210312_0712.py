# Generated by Django 3.1.7 on 2021-03-12 10:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0004_auto_20210311_1937'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='autorizacao_de_fatura',
            field=models.CharField(blank=True, choices=[('apos pc', 'Após PC'), ('apos BMG', 'Após autorizazção assinada BMG'), ('aprovacao pv', 'Aprovação do PV'), ('verbal', 'Verbal')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='cliente',
            name='condicao_de_pagamento',
            field=models.CharField(blank=True, choices=[('28ddl', '28ddl'), ('45ddl', '45ddl'), ('variavel', 'Variável')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='cliente',
            name='incricao_estadual',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='cliente',
            name='metodo_de_cobranca',
            field=models.CharField(blank=True, choices=[('nf+nd', 'NF+ND'), ('nf', 'NF')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='cliente',
            name='regularidade_de_pagamento',
            field=models.CharField(blank=True, choices=[('mensal', 'Mensal'), ('semanal', 'Semanal')], max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='ClienteDocumento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documento', models.FileField(upload_to='documento_cliente')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastro.cliente')),
            ],
        ),
    ]