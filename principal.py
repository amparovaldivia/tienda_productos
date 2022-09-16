from tienda import Tienda
from productos import Productos

tienda=Tienda('pollito')
producto_uno=Productos('lechuga',1000,'verduras')
producto_dos=Productos('tomate',1000,'verduras')
producto_tres=Productos('papas',1000,'verduras')
producto_cuatro=Productos('ajies',200,'verduras')
tienda.agregar_producto(producto_uno).agregar_producto(producto_dos).agregar_producto(producto_tres).agregar_producto(producto_cuatro)
lista_de_productos=[]

tienda.vender_producto(0).vender_producto(2).hacer_liquidación('verduras',0.5).inflación(0.3)

