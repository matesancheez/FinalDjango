"""EntregaFinal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from PreEntrega.views import index, CategoriaH, CategoriaM, CategoriaN, addProduct, addProductM, addProductN





urlpatterns = [
    path("admin/", admin.site.urls),
    path("CategoriaHombre/", CategoriaH, name='hombre'),
    path("addProduct/", addProduct, name='add'),
    path("CategoriaMujer/", CategoriaM, name='mujer'),
    path("addProductM/", addProductM, name='addM'),
    path("CategoriaNinio/", CategoriaN, name='ninio'),
    path("addProductN/", addProductN, name='addN'),
    path("", index, name='index')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)