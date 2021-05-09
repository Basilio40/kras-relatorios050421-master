from django.contrib import admin
from vendas import models
from django.utils.html import format_html

# Register your models here.

class SevicoVendasAdmin(admin.TabularInline):
    model = models.ServicoVenda

class VendasAdmin(admin.ModelAdmin):
    def my_url_field(self, obj):
        return format_html('<a href="{}" target="_blank">Gerar Relatório</a>'.format('/vendas/relatorio/?vendas=' + str(obj.id)))
    my_url_field.allow_tags = True
    my_url_field.short_description = 'Link'

    model = models.Vendas
    list_display = ('id', 'data','my_url_field')
    search_fields = ()
    inlines = [SevicoVendasAdmin ]

admin.site.register(models.Vendas, VendasAdmin)


