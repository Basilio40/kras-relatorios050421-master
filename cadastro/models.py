from django.db import models

# Create your models here.
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
    def __str__(self):
        return self.descricao
    class Meta:
        verbose_name = "Serviço"
        verbose_name_plural = "Serviços"

class Produto(models.Model):
    codigo_produto = models.IntegerField(null=True, blank=True)
    descricao = models.CharField(max_length=100, null=True, blank=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

class ServicoDiverso(models.Model):
    codigo_produto = models.IntegerField(null=True, blank=True)
    descricao = models.CharField(max_length=100, null=True, blank=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    class Meta:
        verbose_name = "Serviço Diverso"
        verbose_name_plural = "Serviços Diversos"


class Colaborador(models.Model):
    CATEGORIA_CHOICES = (
        ('kras', "Kras"),
        ('terceiro', "Terceiro")
    )
    METODO_COBRANCA_CHOICES = (
        ('diaria', "Diária"),
        ('horas', "Horas")
    )
    FORMA_PAGAMENTO_CHOICES = (
        ('boleto', "Boleto"),
        ('debito_conta', "Débito")
    )
    CONDICOES_PAGAMENTO = (
        ('apos-relatorio', "Após a entrega de relatório"),
        ('apos-finalizacao', "Após a finalização do projeto"),
    )   
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    categoria = models.CharField(max_length=100, choices=CATEGORIA_CHOICES)
    metodo_cobranca = models.CharField(max_length=100, choices=METODO_COBRANCA_CHOICES, null=True, blank=True)
    valor_diaria =  models.DecimalField( max_digits=19,decimal_places=10,null=True, blank=True)
    valor_hora = models.DecimalField( max_digits=19,decimal_places=10,null=True, blank=True)
    valor_km = models.DecimalField( max_digits=19,decimal_places=10,null=True, blank=True)
    custo_pedagio = models.CharField(max_length=100,null=True, blank=True)
    custo_in_tinere = models.DecimalField( max_digits=19,decimal_places=10,null=True, blank=True)
    horario_in_tinere = models.CharField(max_length=100, null=True, blank=True)
    endereço = models.CharField(max_length=100,null=True, blank=True)
    cep = models.CharField(max_length=50,null=True, blank=True)
    numero = models.CharField(max_length=50, null=True,blank=True)
    bairro = models.CharField(max_length=100, null=True,blank=True)
    banco_codigo = models.CharField(max_length=100, null=True,blank=True)
    banco_nome = models.CharField(max_length=100, null=True,blank=True)
    agencia = models.CharField(max_length=100, null=True,blank=True)
    conta = models.CharField(max_length=100, null=True,blank=True)
    banco = models.IntegerField(null=True,blank=True)
    cpf = models.CharField(max_length=11, blank=True, null=True)
    CNH = models.CharField(max_length=50, null=True, blank=True)
    validade_CNH = models.DateField(null=True, blank=True)
    forma_pagamento = models.CharField(max_length=100, choices=FORMA_PAGAMENTO_CHOICES, null=True, blank=True)
    valor_contrato = models.DecimalField( max_digits=19,decimal_places=10,null=True, blank=True)
    dia_pagamento = models.IntegerField(null=True, blank=True)
    condicao_pagamento = models.CharField(null=True, blank=True, choices=CONDICOES_PAGAMENTO, max_length=100)
    observacoes = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name_plural = "Colaboradores"

class ColaboradorDocumento(models.Model):
    documento = models.FileField(upload_to="documento_colaborador")
    colaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE)

class ExamesASO(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self):
        return self.nome

class ExamesNR(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self):
        return self.nome

class ColaboradorASO(models.Model):
    colaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE)
    tipo_do_exame = models.ForeignKey(ExamesASO, on_delete=models.CASCADE)
    validade = models.DateField(null=True, blank=True)
    valor_exame = models.DecimalField( max_digits=19,decimal_places=10,null=True, blank=True)
    valor_atualizacao = models.DecimalField( max_digits=19,decimal_places=10,null=True, blank=True)

class ColaboradorNR(models.Model):
    colaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE)
    tipo_do_exame = models.ForeignKey(ExamesNR, on_delete=models.CASCADE)
    valor_exame = models.DecimalField( max_digits=19,decimal_places=10,null=True, blank=True)
    valor_atualizacao = models.DecimalField( max_digits=19,decimal_places=10,null=True, blank=True)
    acessorios = models.DecimalField( max_digits=19,decimal_places=10,null=True, blank=True)

class Compras(models.Model):
    codigo = models.CharField(max_length=50)
    centro_custo = models.CharField(max_length=50)
    descricao_compras = models.CharField(max_length=100, null=True, blank=True)
    unidade = models.CharField(max_length=20, null=True, blank=True)
    def __str__(self):
        return str(self.codigo) + " - " + (self.centro_custo)

class Qualificacao(models.Model):
    descricao = models.CharField(max_length=100)
    def __str__(self):
        return self.descricao
    class Meta:
        verbose_name = "Qualificação"
        verbose_name_plural = "Qualificações"
    
class AtribuicaoDeQualificacao(models.Model):
    colaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE)
    qualificacao = models.ForeignKey(Qualificacao, on_delete=models.CASCADE)
    validade = models.DateField(null=True, blank=True)
    valor_diaria = models.DecimalField(max_digits=6, decimal_places=2)
    valor_de_requalificacao = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        verbose_name = "Qualificação do Colaborador"
        verbose_name_plural = "Qualificações do Colaborador"

class Modalidade(models.Model):
    METODO_COBRANCA_CHOICES = (
        ('diaria', "Diária"),
        ('horas', "Horas"),
        ('quantidade', "Quantidade"),
        ('adicional', "Adicional"),
        ('md -50 / dc +50', "MD -50% / DC +50%")
    )
    centro_custo = models.CharField(max_length=10)
    descricao = models.CharField(max_length=100)
    metodo_de_cobranca = models.CharField(max_length=100, choices=METODO_COBRANCA_CHOICES)
    def __str__(self):
        return self.descricao

class Cliente(models.Model):
    REGULARIDADE_CHOICES = (
        ('mensal', "Mensal"),
        ('semanal', "Semanal"),
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
    METODO_COBRANCA_CHOICES = (
        ('nf+nd', 'NF+ND'),
        ('nf', 'NF')
    )
    AUTORIZACAO_FATURA = (
        ('apos pc', 'Após PC'),
        ('apos BMG', 'Após autorizazção assinada BMG'),
        ('aprovacao pv', "Aprovação do PV"),
        ('verbal', "Verbal")
    )
    nome = models.CharField(max_length=100, unique=True)
    cnpj = models.CharField(max_length=100, null=True, blank=True, unique=True)
    cep = models.CharField(max_length=30, null=True, blank=True)
    rua = models.CharField(max_length=100, null=True, blank=True)
    numero = models.CharField(max_length=20, null=True, blank=True)
    complemento = models.CharField(max_length=100, null=True, blank=True)
    cidade = models.CharField(max_length=100, null=True, blank=True)
    estado = models.CharField(max_length=2, null=True, blank=True)
    incricao_estadual = models.CharField(max_length=100, null=True, blank=True)
    regularidade_de_pagamento = models.CharField(max_length=100, choices=REGULARIDADE_CHOICES, null=True, blank=True)
    condicao_de_pagamento = models.CharField(max_length=100, choices=CONDICAO_CHOICES, null=True, blank=True)
    metodo_de_cobranca = models.CharField(max_length=100, choices=METODO_COBRANCA_CHOICES, null=True, blank=True)
    autorizacao_de_fatura = models.CharField(max_length=100, choices=AUTORIZACAO_FATURA, null=True, blank=True)
    observacoes = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.nome

class ClienteContato(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    contato = models.CharField(max_length=100)
    setor = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    telefone = models.CharField(max_length=100, null=True, blank=True)

class ClienteDocumento(models.Model):
    documento = models.FileField(upload_to="documento_cliente")
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

class ClienteServico(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    valor_deslocamento = models.DecimalField(max_digits=10, decimal_places=2)

class Fornecedor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    telefone = models.CharField(max_length=50, null=True, blank=True)
    cnpj = models.CharField(max_length=100, null=True, blank=True)
    cep = models.CharField(max_length=30, null=True, blank=True)
    rua = models.CharField(max_length=100, null=True, blank=True)
    numero = models.CharField(max_length=20, null=True, blank=True)
    complemento = models.CharField(max_length=100, null=True, blank=True)
    bairro = models.CharField(max_length=100, null=True, blank=True)
    cidade = models.CharField(max_length=100, null=True, blank=True)
    estado = models.CharField(max_length=2, null=True, blank=True)
    observacoes = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name_plural = "Fornecedores"

class FornecedorContato(models.Model):
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    contato = models.CharField(max_length=100)
    setor = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    telefone = models.CharField(max_length=100, null=True, blank=True)

class FornecedorQualificacao(models.Model):
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    qualificacao = models.ForeignKey(Qualificacao, on_delete=models.CASCADE)
    validade = models.DateField(null=True, blank=True)