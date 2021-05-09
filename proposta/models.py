from django.db import models
from cadastro import models as cadastro_models


# Create your models here.
class Proposta(models.Model):
    ATRIBUICAO_CHOICES = (
        ('exe', "Executante"),
        ('resp', "Responsável")
    )
    cliente = models.ForeignKey(cadastro_models.Cliente, on_delete=models.CASCADE)
    responsavel = models.ForeignKey(cadastro_models.Colaborador, on_delete=models.PROTECT, null=True, blank=True, related_name="proposta_responsavel")
    atribuicao = models.CharField(max_length=100, choices=ATRIBUICAO_CHOICES, null=True, blank=True)
    qualificacao = models.ForeignKey(cadastro_models.Qualificacao, on_delete=models.SET_NULL, null=True, blank=True)
    aptidao = models.NullBooleanField(null=True, blank=True)
    ASO = models.NullBooleanField(null=True, blank=True)
    HT = models.FloatField(default=0)
    adicional = models.FloatField(default=0)
    HE = models.FloatField(default=0)
    HE_percentual = models.FloatField(default=0)
    AN = models.FloatField(default=0)
    deslocamento_quilometragem = models.FloatField(default=0)
    pedagio = models.FloatField(default=0)
    outros = models.FloatField(default=0)
    custo = models.FloatField(default=0)
    detalhamento = models.TextField(null=True, blank=True)


    class Meta:
        verbose_name = "Proposta"
        verbose_name_plural = "Propostas"   

class ServicoProposta(models.Model):
    servico = models.ForeignKey(cadastro_models.Servico, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=100, null=True, blank=True)
    descricao = models.CharField(max_length=300, null=True, blank=True)
    valor_servico = models.DecimalField(max_digits=19,decimal_places=3, null=True, blank=True)
    Valor_deslocamento = models.CharField(max_length=100, null=True, blank=True)
    qtd = models.CharField(max_length=100, null=True, blank=True)

    cliente =models.ForeignKey(Proposta, on_delete= models.CASCADE)

    class Meta:
        verbose_name = "Proposta de Serviço"
        verbose_name_plural = "Propostas de Serviço"