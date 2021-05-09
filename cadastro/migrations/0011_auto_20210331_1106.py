# Generated by Django 3.1.7 on 2021-03-31 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0010_auto_20210331_1103'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fornecedor',
            name='contato',
        ),
        migrations.RemoveField(
            model_name='fornecedor',
            name='email_1',
        ),
        migrations.RemoveField(
            model_name='fornecedor',
            name='email_2',
        ),
        migrations.RemoveField(
            model_name='fornecedor',
            name='setor',
        ),
        migrations.RemoveField(
            model_name='fornecedor',
            name='telefone_1',
        ),
        migrations.RemoveField(
            model_name='fornecedor',
            name='telefone_2',
        ),
        migrations.CreateModel(
            name='FornecedorContato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contato', models.CharField(max_length=100)),
                ('setor', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('telefone', models.CharField(blank=True, max_length=100, null=True)),
                ('fornecedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastro.fornecedor')),
            ],
        ),
    ]