from django import template
from django.db.models import fields
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Vendas , ServicoVenda 
from cadastro import models as cadastro_models
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="/admin")
def vendas(request):
    vendas_id = request.GET.get("vendas")
    try:
        vendas = Vendas.objects.get(id=vendas_id)
        servicos = ServicoVenda.objects.filter(venda=vendas)
    except:
        return HttpResponse("400 -  Bad Request.Venda inexistente.", status = 400)
    # OS = ServicoVenda.objects.all()
    # OS = request.GET.get("OS")
    template = loader.get_template("relatorio_vendas.html")
    total = 0
    for item in servicos:
        total = total
    context = {

        "vendas": vendas,
        "servicos": servicos,
        "total": "R$ {:.2f}".format(total)
        # "OS":OS
    }
    return HttpResponse(template.render(context, request))

#+ item.preco_venda
