from django.db import models
from cadastro import models as cadastro_models
import computed_property

# Create your models here.
class Compras(models.Model):
    PC_CHOICES = (
        ('enviado', "Enviado"),
        ('emitido', "Emitido"),
        ('naoemitido', "Não Emitido")
    )
    PAGAMENTO_CHOICE = (
        ('pago', "Pago"),
        ('naopago', "Não Pago")
    )
    METODO_COBRANCA_CHOICES = (
        ('nf+nd', 'NF+ND'),
        ('nf', 'NF')
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
    FORMA_ENTREGA_CHOICES = (
        ('email', 'E-mail'),
        ('retira', 'Retira'),
        ('transportadora', 'Transportadora')
    )
    PC = models.CharField(max_length=100, null=True, blank=True)
    PC_IT = models.CharField(max_length=100, null=True, blank=True)
    status_pc = models.CharField(max_length=100, null=True, blank=True)
    metodo_de_cobranca = models.CharField(max_length=100, choices=METODO_COBRANCA_CHOICES, null=True, blank=True)
    tipo_de_progresso = models.CharField(max_length=100, null=True, blank=True)
    Data = models.DateField(null=True, blank=True)
    status_ps = models.CharField(max_length=100, choices=PC_CHOICES,null=True, blank=True)
    pagamento = models.CharField(max_length=100, choices=PAGAMENTO_CHOICE, null=True, blank=True)
    notafiscal = models.CharField(max_length=150, null=True, blank=True)
    condicao_de_pagamento = models.CharField(max_length=100, choices=CONDICAO_CHOICES, null=True, blank=True)
    metodo_de_pagamento = models.CharField(max_length=100, choices=METODO_PAGAMENTO_CHOICES, null=True, blank=True)
    prazo = models.DateField(null=True, blank=True)
    forma_entrega = models.CharField(max_length=100, null=True, blank=True, choices=FORMA_ENTREGA_CHOICES)
    frases_padrao = models.TextField(blank=True, null=True)
    observacoes = models.TextField(blank=True, null=True)
    fornecedor = models.ForeignKey(cadastro_models.Fornecedor, on_delete=models.SET_NULL, null=True, blank=True)
    imposto = models.CharField(max_length=100, null=True, blank=True)
    porcentagem_impostos = models.DecimalField(max_digits=50, decimal_places=4, default=0.0)
    class Meta:
        verbose_name = "Compra"
        verbose_name_plural = "Compras"

class ItemCompra(models.Model):
    compra = models.ForeignKey(Compras, on_delete=models.CASCADE)
    descricao = models.ForeignKey(cadastro_models.Compras, on_delete=models.SET_NULL, null=True, blank=True)
    detalhamento =  models.CharField(max_length=200, null=True, blank=True)
    unidade = models.CharField(max_length=50, null=True,  blank=True)
    quantidade = models.IntegerField(null=True, blank=True)
    valor = models.DecimalField(max_digits=50, decimal_places=2, default=0.0)
    class Meta:
        verbose_name = "Item da Compra"
        verbose_name_plural = "Itens da Compra"