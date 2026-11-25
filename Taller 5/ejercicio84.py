import os
from enum import Enum
import tkinter as tk
from tkinter import ttk, messagebox, filedialog

class TipoCargo(Enum):
    DIRECTIVO = "Directivo"
    ESTRATEGICO = "Estratégico"
    OPERATIVO = "Operativo"


class TipoGenero(Enum):
    MASCULINO = "Masculino"
    FEMENINO = "Femenino"

class Empleado:
    def __init__(self, nombre: str, apellidos: str, cargo: TipoCargo,
                 genero: TipoGenero, salario_dia: float, dias_trabajados: int,
                 otros_ingresos: float, pagos_salud: float, aporte_pensiones: float):
        self.nombre = nombre
        self.apellidos = apellidos
        self.cargo = cargo
        self.genero = genero
        self.salario_dia = salario_dia
        self.dias_trabajados = dias_trabajados
        self.otros_ingresos = otros_ingresos
        self.pagos_salud = pagos_salud
        self.aporte_pensiones = aporte_pensiones

    def calcular_nomina(self) -> float:
        return (
            (self.salario_dia * self.dias_trabajados)
            + self.otros_ingresos
            - self.pagos_salud
            - self.aporte_pensiones
        )
class ListaEmpleados:
    def __init__(self):
        self.lista: list[Empleado] = []
        self.total_nomina: float = 0.0

    def agregar_empleado(self, empleado: Empleado):
        self.lista.append(empleado)

    def calcular_total_nomina(self) -> float:
        self.total_nomina = sum(e.calcular_nomina() for e in self.lista)
        return self.total_nomina

    def obtener_matriz(self) -> list[tuple]:
        datos = []
        self.total_nomina = 0.0
        for e in self.lista:
            sueldo = e.calcular_nomina()
            datos.append((e.nombre, e.apellidos, f"{sueldo:.2f}"))
            self.total_nomina += sueldo
        return datos

    def convertir_texto(self) -> str:
        texto = ""
        for e in self.lista:
            texto += (
                f"Nombre = {e.nombre}\n"
                f"Apellidos = {e.apellidos}\n"
                f"Cargo = {e.cargo.value}\n"
                f"Género = {e.genero.value}\n"
                f"Salario = ${e.salario_dia}\n"
                f"Días trabajados = {e.dias_trabajados}\n"
                f"Otros ingresos = ${e.otros_ingresos}\n"
                f"Pagos salud = ${e.pagos_salud}\n"
                f"Aportes pensiones = ${e.aporte_pensiones}\n"
                f"---------\n"
            )
        texto += f"Total nómina = ${self.calcular_total_nomina():.2f}"
        return texto
class VentanaAgregarEmpleado(tk.Toplevel):
    def __init__(self, master, lista: ListaEmpleados):
        super().__init__(master)
        self.lista = lista
        self.title("Agregar Empleado")
        self.geometry("320x380")
        self.resizable(False, False)
        self.inicio()

    def inicio(self):
        tk.Label(self, text="Nombre:").place(x=20, y=20)
        self.campo_nombre = tk.Entry(self)
        self.campo_nombre.place(x=160, y=20, width=130)

        tk.Label(self, text="Apellidos:").place(x=20, y=50)
        self.campo_apellidos = tk.Entry(self)
        self.campo_apellidos.place(x=160, y=50, width=130)

        tk.Label(self, text="Cargo:").place(x=20, y=80)
        self.campo_cargo = ttk.Combobox(
            self,
            values=[c.value for c in TipoCargo],
            state="readonly"
        )
        self.campo_cargo.current(0)
        self.campo_cargo.place(x=160, y=80, width=130)

        tk.Label(self, text="Género:").place(x=20, y=110)
        self.var_genero = tk.StringVar(value=TipoGenero.MASCULINO.value)
        tk.Radiobutton(
            self, text="Masculino", variable=self.var_genero, value=TipoGenero.MASCULINO.value
        ).place(x=160, y=110)
        tk.Radiobutton(
            self, text="Femenino", variable=self.var_genero, value=TipoGenero.FEMENINO.value
        ).place(x=160, y=135)

        tk.Label(self, text="Salario por día:").place(x=20, y=170)
        self.campo_salario_dia = tk.Entry(self)
        self.campo_salario_dia.place(x=160, y=170, width=130)

        tk.Label(self, text="Días trabajados al mes:").place(x=20, y=200)
        self.campo_numero_dias = tk.Spinbox(self, from_=1, to=31, width=5)
        self.campo_numero_dias.delete(0, "end")
        self.campo_numero_dias.insert(0, "30")
        self.campo_numero_dias.place(x=160, y=200)

        tk.Label(self, text="Otros ingresos:").place(x=20, y=230)
        self.campo_otros_ingresos = tk.Entry(self)
        self.campo_otros_ingresos.place(x=160, y=230, width=130)

        tk.Label(self, text="Pagos por salud:").place(x=20, y=260)
        self.campo_aportes_salud = tk.Entry(self)
        self.campo_aportes_salud.place(x=160, y=260, width=130)

        tk.Label(self, text="Aportes pensiones:").place(x=20, y=290)
        self.campo_pensiones = tk.Entry(self)
        self.campo_pensiones.place(x=160, y=290, width=130)

        tk.Button(self, text="Agregar", command=self.anadir_empleado).place(x=40, y=330, width=100)
        tk.Button(self, text="Borrar", command=self.limpiar_campos).place(x=170, y=330, width=100)

    def limpiar_campos(self):
        self.campo_nombre.delete(0, tk.END)
        self.campo_apellidos.delete(0, tk.END)
        self.campo_salario_dia.delete(0, tk.END)
        self.campo_numero_dias.delete(0, tk.END)
        self.campo_numero_dias.insert(0, "30")
        self.campo_otros_ingresos.delete(0, tk.END)
        self.campo_aportes_salud.delete(0, tk.END)
        self.campo_pensiones.delete(0, tk.END)

    def anadir_empleado(self):
        try:
            nombre = self.campo_nombre.get().strip()
            apellidos = self.campo_apellidos.get().strip()
            if not nombre or not apellidos:
                raise ValueError("Campos de texto vacíos")

            cargo = TipoCargo(self.campo_cargo.get())
            genero = TipoGenero(self.var_genero.get())
            salario_dia = float(self.campo_salario_dia.get())
            dias_trabajados = int(self.campo_numero_dias.get())
            otros_ingresos = float(self.campo_otros_ingresos.get())
            pagos_salud = float(self.campo_aportes_salud.get())
            aporte_pensiones = float(self.campo_pensiones.get())

            empleado = Empleado(
                nombre, apellidos, cargo, genero,
                salario_dia, dias_trabajados,
                otros_ingresos, pagos_salud, aporte_pensiones
            )
            self.lista.agregar_empleado(empleado)

            messagebox.showinfo("Mensaje", "El empleado ha sido agregado", parent=self)
            self.limpiar_campos()
        except ValueError:
            messagebox.showerror(
                "Error", "Campo nulo o error en formato de número", parent=self
            )


class VentanaNomina(tk.Toplevel):
    def __init__(self, master, lista: ListaEmpleados):
        super().__init__(master)
        self.lista = lista
        self.title("Nómina de Empleados")
        self.geometry("380x260")
        self.resizable(False, False)
        self.inicio()

    def inicio(self):
        tk.Label(self, text="Lista de empleados:").place(x=20, y=10)

        columnas = ("NOMBRE", "APELLIDOS", "SUELDO")
        self.tabla = ttk.Treeview(self, columns=columnas, show="headings", height=6)

        for col in columnas:
            self.tabla.heading(col, text=col)
            self.tabla.column(col, width=110, anchor="center")

        datos = self.lista.obtener_matriz()
        for fila in datos:
            self.tabla.insert("", tk.END, values=fila)

        self.tabla.place(x=20, y=40, width=340, height=150)

        tk.Label(
            self,
            text=f"Total nómina mensual = ${self.lista.total_nomina:.2f}"
        ).place(x=20, y=210)


class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.empleados = ListaEmpleados()
        self.title("Nómina")
        self.geometry("280x380")
        self.resizable(False, False)
        self.inicio()

    def inicio(self):
        barra_menu = tk.Menu(self)
        menu_opciones = tk.Menu(barra_menu, tearoff=0)

        menu_opciones.add_command(label="Agregar empleado", command=self.abrir_agregar_empleado)
        menu_opciones.add_command(label="Calcular nómina", command=self.abrir_nomina)
        menu_opciones.add_separator()
        menu_opciones.add_command(label="Guardar archivo", command=self.guardar_archivo)

        barra_menu.add_cascade(label="Menú", menu=menu_opciones)
        self.config(menu=barra_menu)

    def abrir_agregar_empleado(self):
        VentanaAgregarEmpleado(self, self.empleados)

    def abrir_nomina(self):
        VentanaNomina(self, self.empleados)

    def guardar_archivo(self):
        directorio = filedialog.askdirectory(title="Seleccionar carpeta para guardar")
        if directorio:
            try:
                contenido = self.empleados.convertir_texto()
                ruta_archivo = os.path.join(directorio, "Nómina.txt")
                with open(ruta_archivo, "w", encoding="utf-8") as archivo:
                    archivo.write(contenido)

                messagebox.showinfo(
                    "Mensaje",
                    f"El archivo de la nómina Nómina.txt se ha creado en {directorio}"
                )
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo guardar el archivo:\n{e}")


if __name__ == "__main__":
    app = VentanaPrincipal()
    app.mainloop()