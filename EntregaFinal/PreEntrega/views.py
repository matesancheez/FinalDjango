from django.shortcuts import render
from .models import ProductosH, ProductosM, ProductosN
from .forms import CrearProductosH, CrearProductosM, CrearProductosN

# Create your views here.

def index(request):
    if request.GET.get('nombre', False):
        nombre = request.GET['nombre']
        productos = ProductosH.objects.filter(nombre__icontains=nombre)

        return render(request, 'index.html', {'productos': productos})
    else:
        respuesta = "No se encontraron resultados de su busqueda."
    return render(request, 'index.html', {"respuesta": respuesta})


def addProduct(request):
    data = { 'form': CrearProductosH()} 
    if request.method == "POST":

        producto = CrearProductosH(data=request.POST, files=request.FILES)

        if producto.is_valid():

            producto.save()
            data['mensaje'] = "Se agrego correctamente!!"
        else:
            data["form"] = producto
    
    return render(request, 'producto/AddProducto.html', data)


def addProductM(request):
    data = { 'form': CrearProductosM()} 
    if request.method == "POST":

        producto = CrearProductosM(data=request.POST, files=request.FILES)

        if producto.is_valid():

            producto.save()
            data['mensaje'] = "Se agrego correctamente!!"
        else:
            data["form"] = producto
    
    return render(request, 'producto/AddProductoM.html', data)


def addProductN(request):
    data = { 'form': CrearProductosN()} 
    if request.method == "POST":

        producto = CrearProductosN(data=request.POST, files=request.FILES)

        if producto.is_valid():

            producto.save()
            data['mensaje'] = "Se agrego correctamente!!"
        else:
            data["form"] = producto
    
    return render(request, 'producto/AddProductoN.html', data)


def CategoriaH(request):
    productos = ProductosH.objects.all()

    data = {"productos": productos}

    return render(request, 'producto/hombre.html', data)


def CategoriaM(request):
    productos = ProductosM.objects.all()

    data = {"productos": productos}

    return render(request, 'producto/mujer.html', data)


def CategoriaN(request):
    productos = ProductosN.objects.all()

    data = {"productos": productos}

    return render(request, 'producto/niño.html', data)