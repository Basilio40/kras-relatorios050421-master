# Generated by Django 3.1.7 on 2021-04-01 18:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0011_auto_20210331_1106'),
        ('compras_terceiros', '0003_auto_20210312_0732'),
    ]

    operations = [
        migrations.RenameField(
            model_name='itemcompras',
            old_name='compras',
            new_name='compra',
        ),
        migrations.RemoveField(
            model_name='comprasteceiros',
            name='anormalidade',
        ),
        migrations.RemoveField(
            model_name='comprasteceiros',
            name='custo',
        ),
        migrations.RemoveField(
            model_name='comprasteceiros',
            name='descricao',
        ),
        migrations.RemoveField(
            model_name='comprasteceiros',
            name='desloc_km',
        ),
        migrations.RemoveField(
            model_name='comprasteceiros',
            name='horas_extras',
        ),
        migrations.RemoveField(
            model_name='comprasteceiros',
            name='horas_extras_percentuais',
        ),
        migrations.RemoveField(
            model_name='comprasteceiros',
            name='horas_trabalhadas',
        ),
        migrations.RemoveField(
            model_name='comprasteceiros',
            name='pc_item',
        ),
        migrations.RemoveField(
            model_name='comprasteceiros',
            name='pc_numero',
        ),
        migrations.RemoveField(
            model_name='comprasteceiros',
            name='pedagio',
        ),
        migrations.RemoveField(
            model_name='comprasteceiros',
            name='qtd',
        ),
        migrations.RemoveField(
            model_name='comprasteceiros',
            name='servicos',
        ),
        migrations.RemoveField(
            model_name='comprasteceiros',
            name='tipo',
        ),
        migrations.RemoveField(
            model_name='itemcompras',
            name='nome',
        ),
        migrations.AddField(
            model_name='comprasteceiros',
            name='observacoes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='itemcompras',
            name='anormalidade',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='itemcompras',
            name='data',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='itemcompras',
            name='horas_extras',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='itemcompras',
            name='horas_extras_percentuais',
            field=models.CharField(blank=True, choices=[('50', '50%'), ('75', '75%'), ('100', '100%')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='itemcompras',
            name='horas_trabalhadas',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='itemcompras',
            name='preco',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='itemcompras',
            name='qtd',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='itemcompras',
            name='reembolso',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='itemcompras',
            name='servico',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cadastro.servico'),
        ),
        migrations.CreateModel(
            name='DespesasCompras',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(blank=True, max_length=100, null=True)),
                ('reembolso', models.FloatField(blank=True, null=True)),
                ('preco', models.FloatField(blank=True, null=True)),
                ('compra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compras_terceiros.comprasteceiros')),
            ],
        ),
    ]
