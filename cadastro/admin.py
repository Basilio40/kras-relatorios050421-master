from django.contrib import admin
from cadastro import models
from django import forms
from localflavor.br.forms import BRCNPJField, BRZipCodeField
from input_mask.contrib.localflavor.br.widgets import BRCNPJInput, BRZipCodeInput
# Register your models here.
class ServicoAdmin(admin.ModelAdmin):
    model = models.Servico
    list_display = ('grupo', 'descricao',)
    search_fields = ('descricao',)

class ProdutoAdmin(admin.ModelAdmin):
    model = models.Produto
    list_display = ('id', 'descricao')

class ServicoDiversoAdmin(admin.ModelAdmin):
    model = models.ServicoDiverso
    list_display = ('id', 'descricao')

class AtribuicaoDeQualificacaoAdmin(admin.TabularInline):
    model = models.AtribuicaoDeQualificacao

class ColaboradorDocumentoAdmin(admin.TabularInline):
    model = models.ColaboradorDocumento

class ColaboradorExameAsoAdmin(admin.TabularInline):
    model = models.ColaboradorASO

class ColaboradorExameNRAdmin(admin.TabularInline):
    model = models.ColaboradorNR

class ColaboradorAdmin(admin.ModelAdmin):
    model = models.Colaborador
    list_display = ('nome', 'categoria','valor_diaria','valor_hora','valor_km','endereço',
    'cep','numero','bairro','agencia', 'conta','banco','cpf','forma_pagamento','valor_contrato','dia_pagamento')
    search_fields = ('nome',)
    inlines = [ColaboradorExameAsoAdmin, ColaboradorExameNRAdmin, AtribuicaoDeQualificacaoAdmin, ColaboradorDocumentoAdmin]

class ComprasAdmin(admin.ModelAdmin):
    model = models.Compras
    list_display = ('descricao_compras','unidade',)

class QualificacaoAdmin(admin.ModelAdmin):
    model = models.Qualificacao
    list_display = ('descricao',)
    search_fields = ('descricao',)

class ModalidadeAdmin(admin.ModelAdmin):
    model = models.Modalidade
    list_display = ('centro_custo', 'descricao','metodo_de_cobranca',)
    search_fields = ('descricao',)

class ClienteDocumentoAdmin(admin.TabularInline):
    model = models.ClienteDocumento

class ClienteServicoAdmin(admin.TabularInline):
    model = models.ClienteServico

class ClienteContatoAdmin(admin.TabularInline):
    model = models.ClienteContato

class ClienteForm(forms.ModelForm):
    
    cnpj = BRCNPJField(widget=BRCNPJInput)
    cep = BRZipCodeField(widget=BRZipCodeInput)
    class Meta:
        model = models.Cliente
        fields = '__all__'


class ClienteAdmin(admin.ModelAdmin):
    model = models.Cliente
    form = ClienteForm
    list_display = ('nome','cnpj')
    search_fields = ('nome',)
    inlines = [ClienteContatoAdmin, ClienteDocumentoAdmin, ClienteServicoAdmin]
    class Media:
        js = (
            '//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
        )

class FornecedorQualificacaoAdmin(admin.TabularInline):
    model = models.FornecedorQualificacao

class FornecedorContatoAdmin(admin.TabularInline):
    model = models.FornecedorContato

class FornecedorAdmin(admin.ModelAdmin):
    model = models.Fornecedor
    list_display = ('nome',)
    search_fields = ('nome',)
    inlines = [FornecedorContatoAdmin, FornecedorQualificacaoAdmin,]

class ExamesASOAdmin(admin.ModelAdmin):
    model = models.ExamesASO
    list_display = ('nome',)

class ExamesNRAdmin(admin.ModelAdmin):
    model = models.ExamesNR
    list_display = ("nome",)

admin.site.register(models.Servico, ServicoAdmin)
admin.site.register(models.Produto, ProdutoAdmin)
admin.site.register(models.ServicoDiverso, ServicoDiversoAdmin)
admin.site.register(models.Colaborador, ColaboradorAdmin)
admin.site.register(models.Compras, ComprasAdmin)
admin.site.register(models.Qualificacao, QualificacaoAdmin)
admin.site.register(models.Modalidade, ModalidadeAdmin)
admin.site.register(models.Cliente, ClienteAdmin)
admin.site.register(models.Fornecedor, FornecedorAdmin)
admin.site.register(models.ExamesASO, ExamesASOAdmin)
admin.site.register(models.ExamesNR, ExamesNRAdmin)