from django.contrib import admin
from proposta import models

# Register your models here.

class SevicoPropostaAdmin(admin.TabularInline):
    model = models.ServicoProposta

class PropostaAdmin(admin.ModelAdmin):
    model = models.Proposta
    list_display = ('id','qualificacao','aptidao','custo','HT')
    search_fields = ('id','qualificacao')
    inlines = [SevicoPropostaAdmin ]

admin.site.register(models.Proposta, PropostaAdmin)