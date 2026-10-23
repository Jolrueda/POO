import math
import tkinter as tk
from tkinter import messagebox

class FiguraGeometrica:
    def __init__(self):
        self._volumen = 0.0
        self._superficie = 0.0

    def set_volumen(self, volumen):
        self._volumen = volumen
    def set_superficie(self, superficie):
        self._superficie = superficie
    def get_volumen(self):
        return self._volumen
    def get_superficie(self):
        return self._superficie

class Cilindro(FiguraGeometrica):
    def __init__(self, radio, altura):
        super().__init__()
        self.radio = radio
        self.altura = altura
        self.set_volumen(self.calcular_volumen())
        self.set_superficie(self.calcular_superficie())

    def calcular_volumen(self):
        return math.pi * self.altura * math.pow(self.radio, 2.0)
    def calcular_superficie(self):
        area_lado_a = 2.0 * math.pi * self.radio * self.altura
        area_lado_b = 2.0 * math.pi * math.pow(self.radio, 2.0)
        return area_lado_a + area_lado_b

class Esfera(FiguraGeometrica):
    def __init__(self, radio):
        super().__init__()
        self.radio = radio
        self.set_volumen(self.calcular_volumen())
        self.set_superficie(self.calcular_superficie())

    def calcular_volumen(self):
        return 1.333 * math.pi * math.pow(self.radio, 3.0)
    def calcular_superficie(self):
        return 4.0 * math.pi * math.pow(self.radio, 2.0)

class Piramide(FiguraGeometrica):
    def __init__(self, base, altura, apotema):
        super().__init__()
        self.base = base
        self.altura = altura
        self.apotema = apotema
        self.set_volumen(self.calcular_volumen())
        self.set_superficie(self.calcular_superficie())

    def calcular_volumen(self):
        return (math.pow(self.base, 2.0) * self.altura) / 3.0
    def calcular_superficie(self):
        area_base = math.pow(self.base, 2.0)
        area_lado = 2.0 * self.base * self.apotema
        return area_base + area_lado

class Cubo(FiguraGeometrica):
    def __init__(self, lado):
        super().__init__()
        self.lado = lado
        self.set_volumen(self.calcular_volumen())
        self.set_superficie(self.calcular_superficie())

    def calcular_volumen(self):
        return math.pow(self.lado, 3.0)
    def calcular_superficie(self):
        return 6.0 * math.pow(self.lado, 2.0)

class Prisma(FiguraGeometrica):
    def __init__(self, largo, ancho, altura):
        super().__init__()
        self.largo = largo
        self.ancho = ancho
        self.altura = altura
        self.set_volumen(self.calcular_volumen())
        self.set_superficie(self.calcular_superficie())

    def calcular_volumen(self):
        return self.largo * self.ancho * self.altura
    def calcular_superficie(self):
        return 2.0 * (self.largo * self.ancho + self.largo * self.altura + self.ancho * self.altura)

class VentanaCilindro:
    def __init__(self, root):
        self.root = root
        self.root.title("Cilindro")
        self.root.geometry("400x200") 
        self.root.resizable(False, False)
        self.inicio()

    def inicio(self):
        tk.Label(self.root, text="Radio (cms):", anchor="w").place(x=20, y=20, width=100, height=23)
        self.campo_radio = tk.Entry(self.root)
        self.campo_radio.place(x=100, y=20, width=110, height=23)

        tk.Label(self.root, text="Altura (cms):", anchor="w").place(x=20, y=50, width=100, height=23)
        self.campo_altura = tk.Entry(self.root)
        self.campo_altura.place(x=100, y=50, width=110, height=23)

        tk.Button(self.root, text="Calcular", command=self.calcular_accion).place(x=100, y=80, width=110, height=23)
        
        self.lbl_volumen = tk.Label(self.root, text="Volumen (cm3):", anchor="w")
        self.lbl_volumen.place(x=20, y=110, width=240, height=23)
        
        self.lbl_superficie = tk.Label(self.root, text="Superficie (cm2):", anchor="w")
        self.lbl_superficie.place(x=20, y=140, width=240, height=23)

        try:
            img_original = tk.PhotoImage(file="Img/Cilindro.png") 
            self.img = img_original.subsample(6, 6)
            lbl_imagen = tk.Label(self.root, image=self.img)
            lbl_imagen.image = self.img  
            lbl_imagen.place(x=240, y=20)
        except Exception:
            tk.Label(self.root, text="[Sin imagen]").place(x=240, y=20)
        
    def calcular_accion(self):
        try:
            cilindro = Cilindro(float(self.campo_radio.get()), float(self.campo_altura.get()))
            self.lbl_volumen.config(text=f"Volumen (cm3): {cilindro.get_volumen():.2f}")
            self.lbl_superficie.config(text=f"Superficie (cm2): {cilindro.get_superficie():.2f}")
        except ValueError:
            messagebox.showerror("Error", "Campo nulo o formato incorrecto", parent=self.root)

class VentanaEsfera:
    def __init__(self, root):
        self.root = root
        self.root.title("Esfera")
        self.root.geometry("400x200")
        self.root.resizable(False, False)
        self.inicio()

    def inicio(self):
        tk.Label(self.root, text="Radio (cms):", anchor="w").place(x=20, y=20, width=100, height=23)
        self.campo_radio = tk.Entry(self.root)
        self.campo_radio.place(x=100, y=20, width=110, height=23)

        tk.Button(self.root, text="Calcular", command=self.calcular_accion).place(x=100, y=50, width=110, height=23)
        
        self.lbl_volumen = tk.Label(self.root, text="Volumen (cm3):", anchor="w")
        self.lbl_volumen.place(x=20, y=90, width=240, height=23)
        
        self.lbl_superficie = tk.Label(self.root, text="Superficie (cm2):", anchor="w")
        self.lbl_superficie.place(x=20, y=120, width=240, height=23)

        # Cargar y colocar imagen
        try:
            img_original = tk.PhotoImage(file="Img/Esfera.png") 
            self.img = img_original.subsample(2, 2)
            lbl_imagen = tk.Label(self.root, image=self.img)
            lbl_imagen.image = self.img  
            lbl_imagen.place(x=240, y=20)
        except Exception:
            tk.Label(self.root, text="[Sin imagen]").place(x=240, y=20)
        
    def calcular_accion(self):
        try:
            esfera = Esfera(float(self.campo_radio.get()))
            self.lbl_volumen.config(text=f"Volumen (cm3): {esfera.get_volumen():.2f}")
            self.lbl_superficie.config(text=f"Superficie (cm2): {esfera.get_superficie():.2f}")
        except ValueError:
            messagebox.showerror("Error", "Campo nulo o formato incorrecto", parent=self.root)

class VentanaPiramide:
    def __init__(self, root):
        self.root = root
        self.root.title("Pirámide")
        self.root.geometry("400x220")
        self.root.resizable(False, False)
        self.inicio()

    def inicio(self):
        tk.Label(self.root, text="Base (cms):", anchor="w").place(x=20, y=20, width=100, height=23)
        self.campo_base = tk.Entry(self.root)
        self.campo_base.place(x=120, y=20, width=110, height=23)

        tk.Label(self.root, text="Altura (cms):", anchor="w").place(x=20, y=50, width=100, height=23)
        self.campo_altura = tk.Entry(self.root)
        self.campo_altura.place(x=120, y=50, width=110, height=23)

        tk.Label(self.root, text="Apotema:", anchor="w").place(x=20, y=80, width=100, height=23)
        self.campo_apotema = tk.Entry(self.root)
        self.campo_apotema.place(x=120, y=80, width=110, height=23)

        tk.Button(self.root, text="Calcular", command=self.calcular_accion).place(x=120, y=110, width=110, height=23)
        
        self.lbl_volumen = tk.Label(self.root, text="Volumen (cm3):", anchor="w")
        self.lbl_volumen.place(x=20, y=140, width=240, height=23)
        
        self.lbl_superficie = tk.Label(self.root, text="Superficie (cm2):", anchor="w")
        self.lbl_superficie.place(x=20, y=170, width=240, height=23)

        try:
            img_original = tk.PhotoImage(file="Img/Piramide.png") 
            self.img = img_original.subsample(4, 4)
            lbl_imagen = tk.Label(self.root, image=self.img)
            lbl_imagen.image = self.img  
            lbl_imagen.place(x=250, y=20)
        except Exception:
            tk.Label(self.root, text="[Sin imagen]").place(x=250, y=20)

    def calcular_accion(self):
        try:
            piramide = Piramide(float(self.campo_base.get()), float(self.campo_altura.get()), float(self.campo_apotema.get()))
            self.lbl_volumen.config(text=f"Volumen (cm3): {piramide.get_volumen():.2f}")
            self.lbl_superficie.config(text=f"Superficie (cm2): {piramide.get_superficie():.2f}")
        except ValueError:
            messagebox.showerror("Error", "Campo nulo o formato incorrecto", parent=self.root)

class VentanaCubo:
    def __init__(self, root):
        self.root = root
        self.root.title("Cubo")
        self.root.geometry("400x200")
        self.root.resizable(False, False)
        self.inicio()

    def inicio(self):
        tk.Label(self.root, text="Lado (cms):", anchor="w").place(x=20, y=20, width=100, height=23)
        self.campo_lado = tk.Entry(self.root)
        self.campo_lado.place(x=100, y=20, width=110, height=23)

        tk.Button(self.root, text="Calcular", command=self.calcular_accion).place(x=100, y=50, width=110, height=23)
        
        self.lbl_volumen = tk.Label(self.root, text="Volumen (cm3):", anchor="w")
        self.lbl_volumen.place(x=20, y=90, width=240, height=23)
        
        self.lbl_superficie = tk.Label(self.root, text="Superficie (cm2):", anchor="w")
        self.lbl_superficie.place(x=20, y=120, width=240, height=23)

        try:
            img_original = tk.PhotoImage(file="Img/Cubo.png")
            self.img = img_original.subsample(3, 3)
            lbl_imagen = tk.Label(self.root, image=self.img)
            lbl_imagen.image = self.img  
            lbl_imagen.place(x=240, y=20)
        except Exception:
            tk.Label(self.root, text="[Sin imagen]").place(x=240, y=20)
        
    def calcular_accion(self):
        try:
            cubo = Cubo(float(self.campo_lado.get()))
            self.lbl_volumen.config(text=f"Volumen (cm3): {cubo.get_volumen():.2f}")
            self.lbl_superficie.config(text=f"Superficie (cm2): {cubo.get_superficie():.2f}")
        except ValueError:
            messagebox.showerror("Error", "Campo nulo o formato incorrecto", parent=self.root)

class VentanaPrisma:
    def __init__(self, root):
        self.root = root
        self.root.title("Prisma Rectangular")
        self.root.geometry("400x210")
        self.root.resizable(False, False)
        self.inicio()

    def inicio(self):
        tk.Label(self.root, text="Largo (cms):", anchor="w").place(x=20, y=20, width=100, height=23)
        self.campo_largo = tk.Entry(self.root)
        self.campo_largo.place(x=120, y=20, width=110, height=23)

        tk.Label(self.root, text="Ancho (cms):", anchor="w").place(x=20, y=50, width=100, height=23)
        self.campo_ancho = tk.Entry(self.root)
        self.campo_ancho.place(x=120, y=50, width=110, height=23)

        tk.Label(self.root, text="Altura (cms):", anchor="w").place(x=20, y=80, width=100, height=23)
        self.campo_altura = tk.Entry(self.root)
        self.campo_altura.place(x=120, y=80, width=110, height=23)

        tk.Button(self.root, text="Calcular", command=self.calcular_accion).place(x=120, y=110, width=110, height=23)
        
        self.lbl_volumen = tk.Label(self.root, text="Volumen (cm3):", anchor="w")
        self.lbl_volumen.place(x=20, y=140, width=240, height=23)
        
        self.lbl_superficie = tk.Label(self.root, text="Superficie (cm2):", anchor="w")
        self.lbl_superficie.place(x=20, y=170, width=240, height=23)

        try:
            img_original = tk.PhotoImage(file="Img/Prisma.png")
            self.img = img_original.subsample(3, 3)
            lbl_imagen = tk.Label(self.root, image=self.img)
            lbl_imagen.image = self.img  
            lbl_imagen.place(x=250, y=20)
        except Exception:
            tk.Label(self.root, text="[Sin imagen]").place(x=250, y=20)
        
    def calcular_accion(self):
        try:
            prisma = Prisma(float(self.campo_largo.get()), float(self.campo_ancho.get()), float(self.campo_altura.get()))
            self.lbl_volumen.config(text=f"Volumen (cm3): {prisma.get_volumen():.2f}")
            self.lbl_superficie.config(text=f"Superficie (cm2): {prisma.get_superficie():.2f}")
        except ValueError:
            messagebox.showerror("Error", "Campo nulo o formato incorrecto", parent=self.root)

class VentanaPrincipal:
    def __init__(self, root):
        self.root = root
        self.root.title("Figuras")
        self.root.geometry("380x160") 
        self.root.resizable(False, False)
        self.root.eval('tk::PlaceWindow . center')
        self.inicio()

    def inicio(self):
        tk.Button(self.root, text="Cilindro", command=self.abrir_cilindro).place(x=30, y=30, width=90, height=30)
        tk.Button(self.root, text="Esfera", command=self.abrir_esfera).place(x=140, y=30, width=90, height=30)
        tk.Button(self.root, text="Pirámide", command=self.abrir_piramide).place(x=250, y=30, width=90, height=30)
        
        tk.Button(self.root, text="Cubo", command=self.abrir_cubo).place(x=85, y=80, width=90, height=30)
        tk.Button(self.root, text="Prisma", command=self.abrir_prisma).place(x=195, y=80, width=90, height=30)

    def abrir_cilindro(self):
        VentanaCilindro(tk.Toplevel(self.root))
    def abrir_esfera(self):
        VentanaEsfera(tk.Toplevel(self.root))
    def abrir_piramide(self):
        VentanaPiramide(tk.Toplevel(self.root))
    def abrir_cubo(self):
        VentanaCubo(tk.Toplevel(self.root))
    def abrir_prisma(self):
        VentanaPrisma(tk.Toplevel(self.root))

if __name__ == "__main__":
    ventana_raiz = tk.Tk()
    app = VentanaPrincipal(ventana_raiz)
    ventana_raiz.mainloop()