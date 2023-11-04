import tkinter as tk
from modulo.app import AppAlquilerCompra

class InterfazApp:
    def __init__(self, root):
        self.root = root
        self.root.title("App de Alquiler y Compra de Vehículos")

        self.app = AppAlquilerCompra()
        self.usuario_actual = None

        self.label = tk.Label(root, text="Bienvenido a la aplicación de alquiler y compra de vehículos")
        self.label.pack()

        self.registrar_button = tk.Button(root, text="Registrarse", command=self.mostrar_registro)
        self.registrar_button.pack()

        self.iniciar_sesion_button = tk.Button(root, text="Iniciar Sesión", command=self.mostrar_inicio_sesion)
        self.iniciar_sesion_button.pack()

        self.salir_button = tk.Button(root, text="Salir", command=self.root.quit)
        self.salir_button.pack()

    def mostrar_registro(self):
        self.limpiar_ventana()

        registro_ventana = tk.Toplevel(self.root)
        registro_ventana.title("Registro de Usuario")

        nombre_label = tk.Label(registro_ventana, text="Nombre de usuario:")
        nombre_label.pack()

        self.nombre_entry = tk.Entry(registro_ventana)
        self.nombre_entry.pack()

        contrasena_label = tk.Label(registro_ventana, text="Contraseña:")
        contrasena_label.pack()

        self.contrasena_entry = tk.Entry(registro_ventana, show="*")
        self.contrasena_entry.pack()

        registrar_button = tk.Button(registro_ventana, text="Registrar", command=self.registrar_usuario)
        registrar_button.pack()

    def mostrar_inicio_sesion(self):
        self.limpiar_ventana()

        inicio_ventana = tk.Toplevel(self.root)
        inicio_ventana.title("Iniciar Sesión")

        nombre_label = tk.Label(inicio_ventana, text="Nombre de usuario:")
        nombre_label.pack()

        self.nombre_entry = tk.Entry(inicio_ventana)
        self.nombre_entry.pack()

        contrasena_label = tk.Label(inicio_ventana, text="Contraseña:")
        contrasena_label.pack()

        self.contrasena_entry = tk.Entry(inicio_ventana, show="*")
        self.contrasena_entry.pack()

        iniciar_sesion_button = tk.Button(inicio_ventana, text="Iniciar Sesión", command=self.iniciar_sesion)
        iniciar_sesion_button.pack()

    def mostrar_opciones(self):
        self.limpiar_ventana()
        self.eleccion_label = tk.Label(self.root, text="¿Qué deseas hacer?")
        self.eleccion_label.pack()

        alquilar_button = tk.Button(self.root, text="Alquilar", command=self.mostrar_tipos_vehiculo_alquiler)
        alquilar_button.pack()

        comprar_button = tk.Button(self.root, text="Comprar", command=self.mostrar_tipos_vehiculo_compra)
        comprar_button.pack()

    def mostrar_tipos_vehiculo_alquiler(self):
        self.limpiar_ventana()

        tipo_vehiculo_label = tk.Label(self.root, text="Seleccione el tipo de vehículo (carro o moto) para alquilar:")
        tipo_vehiculo_label.pack()

        alquilar_button = tk.Button(self.root, text="Alquilar", command=self.alquilar_vehiculo)
        alquilar_button.pack()

        self.tipo_vehiculo_alquiler = tk.StringVar()
        carro_radio = tk.Radiobutton(self.root, text="Carro", variable=self.tipo_vehiculo_alquiler, value="carro")
        moto_radio = tk.Radiobutton(self.root, text="Moto", variable=self.tipo_vehiculo_alquiler, value="moto")
        carro_radio.pack()
        moto_radio.pack()

    def alquilar_vehiculo(self):
        tipo_vehiculo = self.tipo_vehiculo_alquiler.get()
        costo_total = self.app.alquilar_vehiculo(self.usuario_actual, tipo_vehiculo, 7)  # Cambiar el número de días según sea necesario
        resultado_label = tk.Label(self.root, text=f"El costo total del alquiler es: ${costo_total}")
        resultado_label.pack()

    def mostrar_tipos_vehiculo_compra(self):
        self.limpiar_ventana()

        tipo_vehiculo_label = tk.Label(self.root, text="Seleccione el tipo de vehículo (carro o moto) para comprar:")
        tipo_vehiculo_label.pack()

        comprar_button = tk.Button(self.root, text="Comprar", command=self.comprar_vehiculo)
        comprar_button.pack()

        self.tipo_vehiculo_compra = tk.StringVar()
        carro_radio = tk.Radiobutton(self.root, text="Carro", variable=self.tipo_vehiculo_compra, value="carro")
        moto_radio = tk.Radiobutton(self.root, text="Moto", variable=self.tipo_vehiculo_compra, value="moto")
        carro_radio.pack()
        moto_radio.pack()

    def comprar_vehiculo(self):
        tipo_vehiculo = self.tipo_vehiculo_compra.get()
        lista_vehiculos = self.app.listar_vehiculos_disponibles(tipo_vehiculo)
        
        lista_vehiculos_str = "\n".join([f"{vehiculo['marca']} - Precio: ${vehiculo['precio']}" for vehiculo in lista_vehiculos])
        
        vehiculos_label = tk.Label(self.root, text=f"Vehículos disponibles:\n{lista_vehiculos_str}")
        vehiculos_label.pack()

    def registrar_usuario(self):
        nombre_usuario = self.nombre_entry.get()
        contrasena = self.contrasena_entry.get()
        resultado = self.app.registrar_usuario(nombre_usuario, contrasena)
        if resultado:
            self.usuario_actual = nombre_usuario
            print(f"Registro exitoso para {nombre_usuario}.")
            self.mostrar_opciones()
        else:
            print("Error al registrar usuario. El nombre de usuario ya existe.")

    def iniciar_sesion(self):
        nombre_usuario = self.nombre_entry.get()
        contrasena = self.contrasena_entry.get()
        if nombre_usuario in self.app.usuarios_registrados and self.app.usuarios_registrados[nombre_usuario].contrasena == contrasena:
            self.usuario_actual = nombre_usuario
            print(f"Iniciaste sesión como {nombre_usuario}.")
            self.mostrar_opciones()
        else:
            print("Nombre de usuario o contraseña incorrectos.")

    def limpiar_ventana(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazApp(root)
    root.mainloop()
