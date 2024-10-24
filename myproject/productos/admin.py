from django.contrib import admin
from .models import Fabrica, Producto

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'precio', 'f_vencimiento', 'fabrica')

admin.site.register(Fabrica)
admin.site.register(Producto, ProductoAdmin)
