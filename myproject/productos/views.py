from django.shortcuts import render
from .models import Fabrica, Producto

def obtener_fabricas_y_productos(request):
    fabricas = Fabrica.objects.raw('SELECT id, nombre FROM productos_fabrica')
    productos = Producto.objects.raw('''
        SELECT p.id, p.nombre, f.nombre as fabrica_nombre
        FROM productos_producto p
        JOIN productos_fabrica f ON p.fabrica_id = f.id
    ''')

    context = {
        'fabricas': fabricas,
        'productos': productos,
    }
    return render(request, 'productos/fabricas_y_productos.html', context)