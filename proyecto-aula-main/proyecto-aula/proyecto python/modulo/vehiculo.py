class Vehiculo:
    def __init__(self, nombre:str, precio_compra:float, stock:int,precio_alquiler:float):
        self.nombre = nombre
        self.precio_compra = precio_compra
        self.stock = stock
        self.precios_alquiler = {}

    def agregar_precio_alquiler (self,dias,precio_alquiler):
        self.precios_alquiler[dias] = precio_alquiler


    def __str__(self):
        return f"Vehículo: {self.nombre} - Precio: ${self.precio_compra} - stock: {self.stock} "