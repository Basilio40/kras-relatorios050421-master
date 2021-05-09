from django.contrib import admin
from ordem_de_servico import models
# Register your models here.

class SevicoAdicionalAdmin(admin.TabularInline):
    model = models.ServicoAdicional

class OrdemAdmin(admin.ModelAdmin):
    model = models.Ordem
    list_display = ('cliente','modalidade', 'executante', 'responsavel', 'entrega_prevista', 'abertura_OS','HT',)
    search_fields = ('cliente','proposta')
    inlines = [SevicoAdicionalAdmin ]

admin.site.register(models.Ordem, OrdemAdmin)
