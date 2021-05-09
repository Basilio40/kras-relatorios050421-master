from django.db import models
from cadastro import models as cadastro_models


# Create your models here.
class ComprasTeceiros(models.Model):
    PC_CHOICES = (
        ('env', "Enviado"),
        ('emit', "Emitido"),
        ('nemit', "Não Emitido"),
    )
    PAGAMENTO_CHOICES = (
        ('pg', "Pago"),
        ('npg', "Não Pago"),
    )
    HEPERCENT_CHOICES = (
        ('50', "50%"),
        ('75', "75%"),
        ('100', "100%"),
    )
    DESPESA_CHOICES = (
        ('despesa',"Despesa"),
        ('servico', "Serviço"),
    )
    CONDICAO_CHOICES = (
        ('28ddl', '28ddl'),
        ('45ddl', '45ddl'),
        ('variavel', 'Variável'),
    )
    METODO_PAGAMENTO_CHOICES = (
        ('boleto', 'Boleto'),
        ('transferencia', 'Transferência Bancária')
    )
    numero_os = models.PositiveIntegerField(default=0)
    data = models.DateField(null=True, blank=True)
    condicao_de_pagamento = models.CharField(max_length=100, choices=CONDICAO_CHOICES, null=True, blank=True)
    metodo_de_pagamento = models.CharField(max_length=100, choices=METODO_PAGAMENTO_CHOICES, null=True, blank=True)
    projeto = models.CharField(max_length=100, null=True, blank=True)
    pedido_compra = models.CharField(max_length=100, choices=PC_CHOICES, null=True, blank=True)
    pagamento_compra = models.CharField(max_length=100, choices=PAGAMENTO_CHOICES,null=True, blank=True)
    notafiscal = models.CharField(max_length=200, null=True, blank=True)
    inspetor = models.ForeignKey(cadastro_models.Colaborador, on_delete=models.SET_NULL, null=True, blank=True)
    observacoes = models.TextField(null=True, blank=True)
    fornecedor = models.ForeignKey(cadastro_models.Fornecedor, on_delete=models.SET_NULL, null=True, blank=True)
    class Meta:
        verbose_name = "Compra de Terceirizada"
        verbose_name_plural = "Compras de Terceiros"


class ItemCompras(models.Model):
    HEPERCENT_CHOICES = (
        ('50', "50%"),
        ('75', "75%"),
        ('100', "100%"),
    )
    compra = models.ForeignKey(ComprasTeceiros, on_delete=models.CASCADE)
    servico = models.ForeignKey(cadastro_models.Servico, on_delete=models.CASCADE, null=True, blank=True)
    data = models.DateField(null=True, blank=True)
    horas_trabalhadas = models.FloatField(null=True, blank=True)
    horas_extras = models.FloatField(null=True, blank=True)
    horas_extras_percentuais = models.CharField(max_length=100, choices=HEPERCENT_CHOICES, null=True, blank=True)
    anormalidade = models.FloatField(null=True, blank=True)
    reembolso = models.FloatField(null=True, blank=True)
    qtd = models.FloatField(null=True, blank=True)
    preco = models.FloatField(null=True, blank=True)
    class Meta:
        verbose_name = "Item da Compra"
        verbose_name_plural = "Itens da Compra"

class DespesasCompras(models.Model):
    compra = models.ForeignKey(ComprasTeceiros, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=100, null=True, blank=True)
    reembolso = models.FloatField(null=True, blank=True)
    preco = models.FloatField(null=True, blank=True)