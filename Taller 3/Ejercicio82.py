import math
import tkinter as tk
from tkinter import messagebox

class Notas:
    def __init__(self):
        self.lista_notas = [0.0] * 5

    def calcular_promedio(self):
        suma = sum(self.lista_notas)
        return suma / len(self.lista_notas)

    def calcular_desviacion(self):
        prom = self.calcular_promedio()
        suma = sum((nota - prom) ** 2 for nota in self.lista_notas)
        return math.sqrt(suma / len(self.lista_notas))

    def calcular_menor(self):
        return min(self.lista_notas)

    def calcular_mayor(self):
        return max(self.lista_notas)


class VentanaPrincipal:
    def __init__(self, root):
        self.root = root
        self.root.title("Notas")
        self.root.geometry("280x380") 
        self.root.resizable(False, False) 
        
        self.root.eval('tk::PlaceWindow . center')
        self.inicio()

    def inicio(self):
        # --- Campos de texto ---
        tk.Label(self.root, text="Nota 1:", anchor="w").place(x=20, y=20, width=80, height=23)
        self.campo_nota1 = tk.Entry(self.root)
        self.campo_nota1.place(x=105, y=20, width=135, height=23)

        tk.Label(self.root, text="Nota 2:", anchor="w").place(x=20, y=50, width=80, height=23)
        self.campo_nota2 = tk.Entry(self.root)
        self.campo_nota2.place(x=105, y=50, width=135, height=23)

        tk.Label(self.root, text="Nota 3:", anchor="w").place(x=20, y=80, width=80, height=23)
        self.campo_nota3 = tk.Entry(self.root)
        self.campo_nota3.place(x=105, y=80, width=135, height=23)

        tk.Label(self.root, text="Nota 4:", anchor="w").place(x=20, y=110, width=80, height=23)
        self.campo_nota4 = tk.Entry(self.root)
        self.campo_nota4.place(x=105, y=110, width=135, height=23)

        tk.Label(self.root, text="Nota 5:", anchor="w").place(x=20, y=140, width=80, height=23)
        self.campo_nota5 = tk.Entry(self.root)
        self.campo_nota5.place(x=105, y=140, width=135, height=23)

        tk.Button(self.root, text="Calcular", command=self.calcular_accion).place(x=20, y=170, width=100, height=23)
        tk.Button(self.root, text="Limpiar", command=self.limpiar_accion).place(x=125, y=170, width=80, height=23)

        self.promedio_lbl = tk.Label(self.root, text="Promedio =", anchor="w")
        self.promedio_lbl.place(x=20, y=210, width=240, height=23)

        self.desviacion_lbl = tk.Label(self.root, text="Desviación estándar =", anchor="w")
        self.desviacion_lbl.place(x=20, y=240, width=240, height=23)

        self.mayor_lbl = tk.Label(self.root, text="Valor mayor =", anchor="w")
        self.mayor_lbl.place(x=20, y=270, width=240, height=23)

        self.menor_lbl = tk.Label(self.root, text="Valor menor =", anchor="w")
        self.menor_lbl.place(x=20, y=300, width=240, height=23)

    def calcular_accion(self):
        val1 = self.campo_nota1.get().strip()
        val2 = self.campo_nota2.get().strip()
        val3 = self.campo_nota3.get().strip()
        val4 = self.campo_nota4.get().strip()
        val5 = self.campo_nota5.get().strip()

        if not val1 or not val2 or not val3 or not val4 or not val5:
            messagebox.showwarning("Datos incompletos", "Es obligatorio ingresar las cinco notas. Por favor, llene todos los campos.")
            return 

        try:
            notas = Notas()
            notas.lista_notas[0] = float(val1)
            notas.lista_notas[1] = float(val2)
            notas.lista_notas[2] = float(val3)
            notas.lista_notas[3] = float(val4)
            notas.lista_notas[4] = float(val5)
        except ValueError:
            messagebox.showerror("Error de formato", "Ha ingresado datos no numéricos. Por favor, ingrese únicamente números (use punto para decimales).")
            return 
     
        self.promedio_lbl.config(text=f"Promedio = {notas.calcular_promedio():.2f}")
        self.desviacion_lbl.config(text=f"Desviación estándar = {notas.calcular_desviacion():.2f}")
        self.mayor_lbl.config(text=f"Valor mayor = {notas.calcular_mayor()}")
        self.menor_lbl.config(text=f"Valor menor = {notas.calcular_menor()}")

    def limpiar_accion(self):
        self.campo_nota1.delete(0, tk.END)
        self.campo_nota2.delete(0, tk.END)
        self.campo_nota3.delete(0, tk.END)
        self.campo_nota4.delete(0, tk.END)
        self.campo_nota5.delete(0, tk.END)
        
        self.promedio_lbl.config(text="Promedio =")
        self.desviacion_lbl.config(text="Desviación estándar =")
        self.mayor_lbl.config(text="Valor mayor =")
        self.menor_lbl.config(text="Valor menor =")

if __name__ == "__main__":
    ventana_raiz = tk.Tk()
    app = VentanaPrincipal(ventana_raiz)
    ventana_raiz.mainloop()