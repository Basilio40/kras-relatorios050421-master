from django.db import models
from cadastro import models as cadastro_models
from proposta import models as proposta 
# Create your models here.
class Ordem(models.Model):
    ATRIBUICAO_CHOICES = (
        ('exe', "Executante"),
        ('resp', "Responsável")
    )
    cliente = models.ForeignKey(cadastro_models.Cliente, on_delete=models.CASCADE)
    modalidade = models.ForeignKey(cadastro_models.Modalidade, on_delete=models.SET_NULL, null=True, blank=True, related_name="modalidade_ordem")
    modalidade_avulsa = models.ForeignKey(cadastro_models.Modalidade, on_delete=models.SET_NULL, null=True, blank=True, related_name="modalidade_ordemavulsa")
    executante = models.ForeignKey(cadastro_models.Colaborador, on_delete=models.PROTECT, null=True, blank=True, related_name="executante_colaborador")
    responsavel = models.ForeignKey(cadastro_models.Colaborador, on_delete=models.PROTECT, null=True, blank=True, related_name="responsavel_colaborador")
    atribuicao = models.CharField(max_length=100, choices=ATRIBUICAO_CHOICES)
    qualificacao = models.ForeignKey(cadastro_models.Qualificacao, on_delete=models.SET_NULL, null=True, blank=True)
    aptidao = models.BooleanField()
    ASO = models.BooleanField()
    entrega_prevista = models.DateTimeField()
    abertura_OS = models.DateTimeField()
    finalizacao_OS = models.DateTimeField(null=True, blank=True)
    HT = models.ForeignKey(proposta.Proposta, on_delete=models.SET_NULL, null=True,blank=True,related_name="proposta_HT" )
    QTD = models.IntegerField(default=0)
    adicional = models.ForeignKey(proposta.Proposta, on_delete=models.PROTECT , null=True,blank=True,related_name="proposta_adicional" )
    HE = models.ForeignKey(proposta.Proposta, on_delete=models.PROTECT , null=True,blank=True,related_name="proposta_HE" )
    HE_percentual = models.ForeignKey(proposta.Proposta, on_delete=models.PROTECT , null=True,blank=True,related_name="proposta_HE_percentual" )
    AN = models.ForeignKey(proposta.Proposta, on_delete=models.PROTECT , null=True,blank=True,related_name="proposta_AN")
    deslocamento_quilometragem = models.ForeignKey(proposta.Proposta, on_delete=models.PROTECT , null=True,blank=True,related_name="proposta_deslocamento")
    pedagio = models.ForeignKey(proposta.Proposta, on_delete=models.PROTECT , null=True,blank=True,related_name="proposta_pedagio")
    outros = models.FloatField(default=0)
    custo = models.ForeignKey(proposta.Proposta, on_delete=models.PROTECT , null=True,blank=True,related_name="proposta_custo")
    detalhamento = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.atribuicao

    class Meta:
        verbose_name = "Ordem de Serviço"
        verbose_name_plural = "Ordens de Serviço"

class Servico(models.Model):
    GRUPO_CHOICES = (
        ('E', 'Externo'),
        ('I', 'Interno')
    )
    METODO_COBRANCA_CHOICES = (
        ('diaria', "Diária"),
        ('horas', "Horas"),
        ('quantidade', "Quantidade"),
        ('adicional', "Adicional"),
        ('md -50 / dc +50', "MD -50% / DC +50%")
    )
    ATRIBUICAO_CHOICES = (
        ('exe', "Executante"),
        ('resp', "Responsável")
    )
    centro_de_custo = models.CharField(max_length=10)
    descricao = models.CharField(max_length=100)
    prazo = models.IntegerField()
    grupo = models.CharField(max_length=100, choices=GRUPO_CHOICES)
    metodo_de_cobranca = models.CharField(max_length=100, choices=METODO_COBRANCA_CHOICES)
    qualificacao = models.CharField(max_length=100)
    atribuicao = models.CharField(max_length=100, choices=ATRIBUICAO_CHOICES)

class ServicoAdicional(models.Model):
    servico = models.ForeignKey(cadastro_models.Servico, on_delete=models.CASCADE)
    valor_servico = models.DecimalField(max_digits=19,decimal_places=3, null=True, blank=True)
    Valor_deslocamento = models.CharField(max_length=100, null=True, blank=True)
    cliente =models.ForeignKey(Ordem, on_delete= models.CASCADE)
    
    class Meta:
        verbose_name = "Serviço"
        verbose_name_plural = "Serviços"

