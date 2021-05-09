"""kras URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from compras import views as compras_views
from compras_terceiros import views as compras_terceiros_views
from vendas import views as vendas_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path("compras/relatorio/", compras_views.compra),
    path("compras_terceiros/relatorio/", compras_terceiros_views.compra),
    path("vendas/relatorio/", vendas_views.vendas)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'Kras Engenharia'
admin.site.index_title  = 'Sistema'
admin.site.site_title = "Kras Engenharia"