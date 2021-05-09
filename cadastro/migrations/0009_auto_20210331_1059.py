# Generated by Django 3.1.7 on 2021-03-31 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0008_clienteservico'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_produto', models.IntegerField(blank=True, null=True)),
                ('descricao', models.CharField(blank=True, max_length=100, null=True)),
                ('valor', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ServicoDiverso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_produto', models.IntegerField(blank=True, null=True)),
                ('descricao', models.CharField(blank=True, max_length=100, null=True)),
                ('valor', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
            options={
                'verbose_name': 'Serviço Diverso',
                'verbose_name_plural': 'Serviços Diversos',
            },
        ),
        migrations.AddField(
            model_name='cliente',
            name='observacoes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='colaborador',
            name='observacoes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='fornecedor',
            name='observacoes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='FornecedorQualificacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('validade', models.DateField(blank=True, null=True)),
                ('fornecedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastro.fornecedor')),
                ('qualificacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastro.qualificacao')),
            ],
        ),
    ]
