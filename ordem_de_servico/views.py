from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Ordem
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url="/admin")
def ordem_servico(request):
    ordem_id = request.GET.get("ordem")
    try:
        ordem = Ordem.objects.get(id=ordem_id)
    except:
        return HttpResponse("400 - Bad Request. Compra inexistente.", status=400)
    ordem = Ordem.objects.filter(ordem=ordem)
    template = loader.get_template("relatorio.html")   
    context = {
        "ordem": ordem,
       
    }
    return HttpResponse(template.render(context, request))
