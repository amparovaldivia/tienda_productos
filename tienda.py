from productos import Productos
class Tienda:
    def __init__(self,nombre):
        self.nombre=nombre
        self.lista_de_productos=[]


    def agregar_producto(self, nuevo_producto):
        self.lista_de_productos.append(nuevo_producto)
        return self
    def vender_producto(self, id): 
        x= self.lista_de_productos.pop(id)
        print(x.__dict__)
        return self
    def inflación(self, porcentaje_aumento): 
        for producto in self.lista_de_productos:
            producto.actualizar_precio(porcentaje_aumento,True)
        return self
    def hacer_liquidación(self, category,porcentaje_descuento): 
        for producto in self.lista_de_productos:
            if producto.categoria == category:
                producto.actualizar_precio(porcentaje_descuento,False)
        return self 

