class Productos:
    def __init__(self,nombre,precio,categoria) -> None:
        self.nombre=nombre
        self.precio=precio
        self.categoria=categoria


    def actualizar_precio(self, cambio_porcentaje, esta_elevado): 
        if  esta_elevado==True:
            self.precio=self.precio*(1+cambio_porcentaje)
        else:
            self.precio=self.precio*(1-cambio_porcentaje)

    def  Print_info(self):
        print(self.__dict__)