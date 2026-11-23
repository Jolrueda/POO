import math
import tkinter as tk
from tkinter import ttk, messagebox


class CalculosNumericos:
    @staticmethod
    def calcular_logaritmo_neperiano(valor):
        if not isinstance(valor, (int, float)) or isinstance(valor, bool):
            raise TypeError("El valor debe ser numérico para calcular el logaritmo.")
        if valor <= 0:
            raise ValueError("El valor debe ser un número positivo mayor a 0.")
        return math.log(valor)

    @staticmethod
    def calcular_raiz_cuadrada(valor):
        if not isinstance(valor, (int, float)) or isinstance(valor, bool):
            raise TypeError("El valor debe ser numérico para calcular la raíz cuadrada.")
        if valor < 0:
            raise ValueError("El valor debe ser un número positivo (>= 0).")
        return math.sqrt(valor)

    @staticmethod
    def calcular_pendiente(x1, y1, x2, y2):
        puntos = [x1, y1, x2, y2]
        if any(not isinstance(p, (int, float)) or isinstance(p, bool) for p in puntos):
            raise TypeError("Todas las coordenadas deben ser valores numéricos.")
        if x1 == x2:
            raise ZeroDivisionError("La recta es vertical (x1 = x2). La pendiente es indefinida.")
        return (y2 - y1) / (x2 - x1)

    @staticmethod
    def calcular_punto_medio(x1, y1, x2, y2):
        puntos = [x1, y1, x2, y2]
        if any(not isinstance(p, (int, float)) or isinstance(p, bool) for p in puntos):
            raise TypeError("Todas las coordenadas deben ser valores numéricos.")
        mx = (x1 + x2) / 2
        my = (y1 + y2) / 2
        return mx, my

    @staticmethod
    def calcular_raices_cuadratica(a, b, c):
        coefs = [a, b, c]
        if any(not isinstance(k, (int, float)) or isinstance(k, bool) for k in coefs):
            raise TypeError("Los coeficientes deben ser valores numéricos.")
        if a == 0:
            raise ZeroDivisionError("El coeficiente 'a' no puede ser 0 en una ecuación cuadrática.")

        discriminante = (b ** 2) - (4 * a * c)
        if discriminante < 0:
            raise ValueError("El discriminante es negativo. La ecuación no tiene raíces reales.")

        x1 = (-b + math.sqrt(discriminante)) / (2 * a)
        x2 = (-b - math.sqrt(discriminante)) / (2 * a)
        return x1, x2

    @staticmethod
    def convertir_base_10_a_base_b(numero, base):
        if not isinstance(numero, int) or not isinstance(base, int) or isinstance(numero, bool) or isinstance(base, bool):
            raise TypeError("El número y la base deben ser enteros válidos.")
        if numero < 0:
            raise ValueError("El número a convertir debe ser un entero no negativo.")
        if base < 2 or base > 36:
            raise ValueError("La base debe estar comprendida entre 2 y 36.")

        if numero == 0:
            return "0"

        caracteres = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        resultado = ""
        n = numero

        while n > 0:
            residuo = n % base
            resultado = caracteres[residuo] + resultado
            n //= base

        return resultado


class AppCalculadora(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora de Cálculos Numéricos")
        self.geometry("450x400")
        self.resizable(False, False)

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=10)

        self._crear_pestana_log_raiz()
        self._crear_pestana_recta()
        self._crear_pestana_cuadratica()
        self._crear_pestana_base()


    def _crear_pestana_log_raiz(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Log / Raíz")

        ttk.Label(frame, text="Ingrese un valor numérico:").pack(pady=10)
        entry_val = ttk.Entry(frame, justify="center")
        entry_val.pack(pady=5)

        lbl_resultado = ttk.Label(frame, text="Resultado: -", font=("Arial", 10, "bold"))
        lbl_resultado.pack(pady=15)

        def ejecutar_log():
            try:
                val = float(entry_val.get())
                res = CalculosNumericos.calcular_logaritmo_neperiano(val)
                lbl_resultado.config(text=f"Log. Neperiano: {res:.4f}")
            except (ValueError, TypeError) as e:
                messagebox.showerror("Error de Cálculo", str(e))

        def ejecutar_raiz():
            try:
                val = float(entry_val.get())
                res = CalculosNumericos.calcular_raiz_cuadrada(val)
                lbl_resultado.config(text=f"Raíz Cuadrada: {res:.4f}")
            except (ValueError, TypeError) as e:
                messagebox.showerror("Error de Cálculo", str(e))

        btn_box = ttk.Frame(frame)
        btn_box.pack(pady=10)
        ttk.Button(btn_box, text="Logaritmo", command=ejecutar_log).pack(side="left", padx=5)
        ttk.Button(btn_box, text="Raíz Cuadrada", command=ejecutar_raiz).pack(side="left", padx=5)

    def _crear_pestana_recta(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Geometría Recta")

        grid_frame = ttk.Frame(frame)
        grid_frame.pack(pady=10)

        labels = ["Punto 1 (x1, y1):", "Punto 2 (x2, y2):"]
        ttk.Label(grid_frame, text=labels[0]).grid(row=0, column=0, columnspan=2, pady=5)
        ttk.Label(grid_frame, text=labels[1]).grid(row=2, column=0, columnspan=2, pady=5)

        entry_x1 = ttk.Entry(grid_frame, width=8, justify="center")
        entry_y1 = ttk.Entry(grid_frame, width=8, justify="center")
        entry_x2 = ttk.Entry(grid_frame, width=8, justify="center")
        entry_y2 = ttk.Entry(grid_frame, width=8, justify="center")

        entry_x1.grid(row=1, column=0, padx=5)
        entry_y1.grid(row=1, column=1, padx=5)
        entry_x2.grid(row=3, column=0, padx=5)
        entry_y2.grid(row=3, column=1, padx=5)

        lbl_resultado = ttk.Label(frame, text="Resultado: -", font=("Arial", 10, "bold"))
        lbl_resultado.pack(pady=15)

        def obtener_coordenadas():
            return float(entry_x1.get()), float(entry_y1.get()), float(entry_x2.get()), float(entry_y2.get())

        def ejecutar_pendiente():
            try:
                x1, y1, x2, y2 = obtener_coordenadas()
                res = CalculosNumericos.calcular_pendiente(x1, y1, x2, y2)
                lbl_resultado.config(text=f"Pendiente (m): {res:.4f}")
            except (ValueError, TypeError, ZeroDivisionError) as e:
                messagebox.showerror("Error de Recta", str(e))

        def ejecutar_punto_medio():
            try:
                x1, y1, x2, y2 = obtener_coordenadas()
                mx, my = CalculosNumericos.calcular_punto_medio(x1, y1, x2, y2)
                lbl_resultado.config(text=f"Punto Medio (M): ({mx:.2f}, {my:.2f})")
            except (ValueError, TypeError) as e:
                messagebox.showerror("Error de Recta", str(e))

        btn_box = ttk.Frame(frame)
        btn_box.pack(pady=10)
        ttk.Button(btn_box, text="Pendiente", command=ejecutar_pendiente).pack(side="left", padx=5)
        ttk.Button(btn_box, text="Punto Medio", command=ejecutar_punto_medio).pack(side="left", padx=5)

    def _crear_pestana_cuadratica(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Cuadrática")

        ttk.Label(frame, text="Ecuación: ax² + bx + c = 0").pack(pady=10)

        grid_frame = ttk.Frame(frame)
        grid_frame.pack(pady=5)

        ttk.Label(grid_frame, text="a:").grid(row=0, column=0, padx=2)
        entry_a = ttk.Entry(grid_frame, width=6, justify="center")
        entry_a.grid(row=0, column=1, padx=5)

        ttk.Label(grid_frame, text="b:").grid(row=0, column=2, padx=2)
        entry_b = ttk.Entry(grid_frame, width=6, justify="center")
        entry_b.grid(row=0, column=3, padx=5)

        ttk.Label(grid_frame, text="c:").grid(row=0, column=4, padx=2)
        entry_c = ttk.Entry(grid_frame, width=6, justify="center")
        entry_c.grid(row=0, column=5, padx=5)

        lbl_resultado = ttk.Label(frame, text="Raíces: -", font=("Arial", 10, "bold"))
        lbl_resultado.pack(pady=15)

        def ejecutar_cuadratica():
            try:
                a = float(entry_a.get())
                b = float(entry_b.get())
                c = float(entry_c.get())
                x1, x2 = CalculosNumericos.calcular_raices_cuadratica(a, b, c)

                if x1 == x2:
                    lbl_resultado.config(text=f"Raíz única (x): {x1:.4f}")
                else:
                    lbl_resultado.config(text=f"x1: {x1:.4f}  |  x2: {x2:.4f}")
            except (ValueError, TypeError, ZeroDivisionError) as e:
                messagebox.showerror("Error Cuadrático", str(e))

        ttk.Button(frame, text="Calcular Raíces", command=ejecutar_cuadratica).pack(pady=10)

    def _crear_pestana_base(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Cambio de Base")

        grid_frame = ttk.Frame(frame)
        grid_frame.pack(pady=15)

        ttk.Label(grid_frame, text="Número (Base 10):").grid(row=0, column=0, sticky="e", pady=5)
        entry_num = ttk.Entry(grid_frame, width=12, justify="center")
        entry_num.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(grid_frame, text="Base destino (2-36):").grid(row=1, column=0, sticky="e", pady=5)
        entry_base = ttk.Entry(grid_frame, width=12, justify="center")
        entry_base.grid(row=1, column=1, padx=5, pady=5)

        lbl_resultado = ttk.Label(frame, text="Resultado: -", font=("Arial", 10, "bold"))
        lbl_resultado.pack(pady=15)

        def ejecutar_conversion():
            try:
                num = int(entry_num.get())
                base = int(entry_base.get())
                res = CalculosNumericos.convertir_base_10_a_base_b(num, base)
                lbl_resultado.config(text=f"Base {base}: {res}")
            except (ValueError, TypeError) as e:
                messagebox.showerror("Error de Conversión", str(e))

        ttk.Button(frame, text="Convertir", command=ejecutar_conversion).pack(pady=10)


if __name__ == "__main__":
    app = AppCalculadora()
    app.mainloop()