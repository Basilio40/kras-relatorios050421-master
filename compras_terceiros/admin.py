from django.contrib import admin
from compras_terceiros import models
from django.utils.html import format_html

# Register your models here.

class ComprasItemAdmin(admin.TabularInline):
    model = models.ItemCompras

class ComprasDespesaAdmin(admin.TabularInline):
    model = models.DespesasCompras

class ComprasTerceirosAdmin(admin.ModelAdmin):
    def my_url_field(self, obj):
        return format_html('<a href="{}" target="_blank">Gerar Relatório</a>'.format('/compras_terceiros/relatorio/?compra=' + str(obj.id)))
    my_url_field.allow_tags = True
    my_url_field.short_description = 'Link'

    model = models.ComprasTeceiros
    list_display = ('numero_os', 'projeto', 'my_url_field')
    inlines = [ComprasItemAdmin, ComprasDespesaAdmin]
    
admin.site.register(models.ComprasTeceiros, ComprasTerceirosAdmin)

