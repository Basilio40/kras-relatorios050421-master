from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import ComprasTeceiros, ItemCompras, DespesasCompras
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.

@login_required(login_url="/admin")
def compra(request):
    compra_id = request.GET.get("compra")
    try:
        compra = ComprasTeceiros.objects.get(id=compra_id)
    except:
        return HttpResponse("400 - Bad Request. Compra inexistente.", status=400)
    compra_itens = ItemCompras.objects.filter(compra=compra)
    compra_despesas = DespesasCompras.objects.filter(compra=compra)
    template = loader.get_template("relatorio.html")
    total = 0
    total_despesas = 0
    for item in compra_itens:
        try: total = total + item.qtd * item.preco
        except: print(item)
    for item in compra_despesas:
        total_despesas = total_despesas 
    context = {
        "compra": compra,
        "itens": compra_itens,
        "despesa": compra_despesas,
        "total": "R$ {:.2f}".format(total),
        "total_despesas": "R$ {:.2f}".format(total_despesas)
    }
    return HttpResponse(template.render(context, request))

    #
    # + item.preco