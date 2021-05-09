from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Compras, ItemCompra
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url="/admin")
def compra(request):
    compra_id = request.GET.get("compra")
    try:
        compra = Compras.objects.get(id=compra_id)
    except:
        return HttpResponse("400 - Bad Request. Compra inexistente.", status=400)
    compra_itens = ItemCompra.objects.filter(compra=compra)
    template = loader.get_template("relatorio.html")
    subtotal = 0
    for item in compra_itens:
        try:subtotal = subtotal*compra.porcentagem_impostos/100
        except: print(item)
    impostos = subtotal + item.quantidade * item.valor
    total = subtotal + impostos   
    context = {
        "compra": compra,
        "itens": compra_itens,
        "subtotal": "R$ {:.2f}".format(subtotal),
        "total": "R$ {:.2f}".format(total),
        "impostos": "R$ {:.2f}".format(impostos)
    }
    return HttpResponse(template.render(context, request))

    
    