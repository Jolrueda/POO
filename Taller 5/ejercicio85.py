import tkinter as tk
from tkinter import messagebox, simpledialog
from datetime import datetime
class Huesped:
    def __init__(self, nombres, apellidos, documento_identidad, fecha_ingreso):
        self.nombres = nombres
        self.apellidos = apellidos
        self.documento_identidad = documento_identidad
        self.fecha_ingreso = fecha_ingreso
        self.fecha_salida = None

    def obtener_dias_alojamiento(self):
        if self.fecha_salida and self.fecha_ingreso:
            dias = (self.fecha_salida - self.fecha_ingreso).days
            return dias if dias > 0 else 0
        return 0

class Habitacion:
    def __init__(self, numero, disponible, precio_dia):
        self.numero = numero
        self.disponible = disponible
        self.precio_dia = precio_dia
        self.huesped = None

class Hotel:
    def __init__(self):
        self.habitaciones = []
        for i in range(1, 11):
            precio = 120000 if i <= 5 else 160000
            self.habitaciones.append(Habitacion(i, True, precio))

    def buscar_fecha_ingreso(self, numero):
        for hab in self.habitaciones:
            if hab.numero == numero and hab.huesped:
                return hab.huesped.fecha_ingreso.strftime("%Y-%m-%d")
        return ""

    def buscar_habitacion_ocupada(self, numero):
        for hab in self.habitaciones:
            if hab.numero == numero and not hab.disponible:
                return True
        return False

    def obtener_habitacion(self, numero):
        for hab in self.habitaciones:
            if hab.numero == numero:
                return hab
        return None

class VentanaPrincipal(tk.Tk):
    def __init__(self, hotel):
        super().__init__()
        self.hotel = hotel
        self.title("Hotel")
        self.geometry("300x200")
        self.eval('tk::PlaceWindow . center')
        
        barra_menu = tk.Menu(self)
        menu_opciones = tk.Menu(barra_menu, tearoff=0)
        menu_opciones.add_command(label="Consultar habitaciones", command=self.abrir_habitaciones)
        menu_opciones.add_command(label="Salida de huéspedes", command=self.abrir_salida)
        barra_menu.add_cascade(label="Menú", menu=menu_opciones)
        self.config(menu=barra_menu)

    def abrir_habitaciones(self):
        VentanaHabitaciones(self, self.hotel)

    def abrir_salida(self):
        numero = simpledialog.askinteger("Salida de huéspedes", "Ingrese número de habitación (1-10):", parent=self, minvalue=1, maxvalue=10)
        if numero:
            if self.hotel.buscar_habitacion_ocupada(numero):
                VentanaSalida(self, self.hotel, numero)
            else:
                messagebox.showinfo("Mensaje", "La habitación ingresada no ha sido ocupada o no existe.")

class VentanaHabitaciones(tk.Toplevel):
    def __init__(self, parent, hotel):
        super().__init__(parent)
        self.hotel = hotel
        self.title("Habitaciones")
        self.geometry("600x200")
        
        for i, hab in enumerate(self.hotel.habitaciones):
            fila = 0 if i < 5 else 2
            columna = i % 5
            
            tk.Label(self, text=f"Habitación {hab.numero}").grid(row=fila, column=columna, padx=15, pady=10)
            estado = "Disponible" if hab.disponible else "No disponible"
            tk.Label(self, text=estado, fg="green" if hab.disponible else "red").grid(row=fila+1, column=columna)

        tk.Label(self, text="Habitación a reservar:").grid(row=4, column=1, columnspan=2, pady=20, sticky="e")
        self.spinbox = tk.Spinbox(self, from_=1, to=10, width=5)
        self.spinbox.grid(row=4, column=3, sticky="w")
        
        tk.Button(self, text="Aceptar", command=self.aceptar).grid(row=4, column=4)

    def aceptar(self):
        try:
            num = int(self.spinbox.get())
            if self.hotel.buscar_habitacion_ocupada(num):
                messagebox.showinfo("Mensaje", "La habitación está ocupada")
            else:
                VentanaIngreso(self.master, self.hotel, num)
                self.destroy()
        except ValueError:
            messagebox.showerror("Error", "Número de habitación inválido")

class VentanaIngreso(tk.Toplevel):
    def __init__(self, parent, hotel, numero_hab):
        super().__init__(parent)
        self.hotel = hotel
        self.numero_hab = numero_hab
        self.title("Ingreso")
        self.geometry("300x250")

        tk.Label(self, text=f"Habitación: {self.numero_hab}").grid(row=0, column=0, columnspan=2, pady=5)
        
        tk.Label(self, text="Fecha (aaaa-mm-dd):").grid(row=1, column=0, sticky="e")
        self.fecha_ent = tk.Entry(self)
        self.fecha_ent.grid(row=1, column=1)

        tk.Label(self, text="Huésped", font=("Arial", 10, "bold")).grid(row=2, column=0, columnspan=2, pady=5)

        tk.Label(self, text="Nombre:").grid(row=3, column=0, sticky="e")
        self.nombre_ent = tk.Entry(self)
        self.nombre_ent.grid(row=3, column=1)

        tk.Label(self, text="Apellidos:").grid(row=4, column=0, sticky="e")
        self.apellidos_ent = tk.Entry(self)
        self.apellidos_ent.grid(row=4, column=1)

        tk.Label(self, text="Doc. Identidad:").grid(row=5, column=0, sticky="e")
        self.doc_ent = tk.Entry(self)
        self.doc_ent.grid(row=5, column=1)

        tk.Button(self, text="Aceptar", command=self.registrar).grid(row=6, column=0, pady=15)
        tk.Button(self, text="Cancelar", command=self.destroy).grid(row=6, column=1, pady=15)

    def registrar(self):
        try:
            fecha = datetime.strptime(self.fecha_ent.get(), "%Y-%m-%d")
            doc = int(self.doc_ent.get())
            nombre = self.nombre_ent.get()
            apellido = self.apellidos_ent.get()
            
            if not nombre or not apellido:
                raise ValueError("Campos vacíos")

            huesped = Huesped(nombre, apellido, doc, fecha)
            hab = self.hotel.obtener_habitacion(self.numero_hab)
            hab.huesped = huesped
            hab.disponible = False

            messagebox.showinfo("Mensaje", "El huésped ha sido registrado")
            self.destroy()
        except ValueError as e:
            if "time data" in str(e):
                messagebox.showerror("Error", "La fecha no está en el formato solicitado")
            else:
                messagebox.showerror("Error", "Campo nulo o error en formato de número")

class VentanaSalida(tk.Toplevel):
    def __init__(self, parent, hotel, numero_hab):
        super().__init__(parent)
        self.hotel = hotel
        self.hab = self.hotel.obtener_habitacion(numero_hab)
        self.title("Salida huéspedes")
        self.geometry("300x250")

        tk.Label(self, text=f"Habitación: {self.hab.numero}").grid(row=0, column=0, pady=5)
        
        fecha_ing = self.hotel.buscar_fecha_ingreso(self.hab.numero)
        tk.Label(self, text=f"Fecha de ingreso: {fecha_ing}").grid(row=1, column=0, pady=2)
        
        tk.Label(self, text="Fecha de salida (aaaa-mm-dd):").grid(row=2, column=0, pady=2)
        self.fecha_salida_ent = tk.Entry(self)
        self.fecha_salida_ent.grid(row=3, column=0)

        tk.Button(self, text="Calcular", command=self.calcular).grid(row=4, column=0, pady=5)

        self.lbl_dias = tk.Label(self, text="Cantidad de días: ")
        self.lbl_dias.grid(row=5, column=0)

        self.lbl_total = tk.Label(self, text="Total: $")
        self.lbl_total.grid(row=6, column=0)

        self.btn_registrar = tk.Button(self, text="Registrar Salida", command=self.registrar_salida, state=tk.DISABLED)
        self.btn_registrar.grid(row=7, column=0, pady=10)

    def calcular(self):
        try:
            fecha_salida = datetime.strptime(self.fecha_salida_ent.get(), "%Y-%m-%d")
            
            if fecha_salida <= self.hab.huesped.fecha_ingreso:
                messagebox.showerror("Mensaje", "La fecha de salida es menor o igual que la de ingreso")
                return

            self.hab.huesped.fecha_salida = fecha_salida
            dias = self.hab.huesped.obtener_dias_alojamiento()
            total = dias * self.hab.precio_dia

            self.lbl_dias.config(text=f"Cantidad de días: {dias}")
            self.lbl_total.config(text=f"Total: ${total:.1f}")
            self.btn_registrar.config(state=tk.NORMAL)

        except ValueError:
            messagebox.showerror("Mensaje", "La fecha no está en el formato solicitado")

    def registrar_salida(self):
        self.hab.huesped = None
        self.hab.disponible = True
        messagebox.showinfo("Mensaje", "Se ha registrado la salida del huésped")
        self.destroy()

if __name__ == "__main__":
    app_hotel = Hotel()
    app = VentanaPrincipal(app_hotel)
    app.mainloop()