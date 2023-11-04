class Usuario:
    def __init__(self, nombre_usuario, contrasena):
        self.nombre_usuario = nombre_usuario
        self.contrasena = contrasena

    def __str__(self):
        return f"Usuario: {self.nombre_usuario}"