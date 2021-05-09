from django.contrib import admin
from compras import models
from django.utils.html import format_html
# Register your models here.


class ItemComprasAdmin(admin.TabularInline):
    model = models.ItemCompra

class ComprasAdmin(admin.ModelAdmin):
    model = models.Compras
    list_display = ('PC', 'Data', 'my_url_field')
    readonly_fields = ("valor_imposto","valor_total",)

    def my_url_field(self, obj):
        return format_html('<a href="{}" target="_blank">Gerar Relatório</a>'.format('/compras/relatorio/?compra=' + str(obj.id)))
    my_url_field.allow_tags = True
    my_url_field.short_description = 'Link'

    def valor_imposto(self, obj):
        return "R$ 0"
       
    def valor_total(self, obj):
        return "R$ 0"
    
    inlines = [ItemComprasAdmin]
    
    class Media:
        js = (
            '//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            "compras/calculos.js",
        )

admin.site.register(models.Compras, ComprasAdmin)


