import tkinter as tk
from tkinter import ttk, messagebox

class AplicacionExcepciones(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Prueba de Excepciones")
        self.geometry("520x450")
        self.resizable(False, False)
        
        estilo = ttk.Style(self)
        estilo.theme_use("clam")
        
        # Título principal
        label_titulo = ttk.Label(
            self, 
            text="Simulador de Excepciones en Python", 
            font=("Helvetica", 14, "bold")
        )
        label_titulo.pack(pady=10)

        frame_botones = ttk.Frame(self)
        frame_botones.pack(pady=10, fill="x", padx=20)

        boton_prueba1 = ttk.Button(
            frame_botones, 
            text="Prueba Excepciones (Try 1 & 2)", 
            command=self.prueba_excepciones
        )
        boton_prueba1.pack(fill="x", pady=4)

        boton_prueba2 = ttk.Button(
            frame_botones, 
            text="Excepción Fuera de Límite", 
            command=self.excepcion_fuera_limite
        )
        boton_prueba2.pack(fill="x", pady=4)

        boton_prueba3 = ttk.Button(
            frame_botones, 
            text="Excepción Formato Número", 
            command=self.excepcion_formato_numero
        )
        boton_prueba3.pack(fill="x", pady=4)

        boton_limpiar = ttk.Button(
            frame_botones, 
            text="Limpiar Consola", 
            command=self.limpiar_log
        )
        boton_limpiar.pack(fill="x", pady=4)

        label_consola = ttk.Label(self, text="Salida del Programa:", font=("Helvetica", 10, "bold"))
        label_consola.pack(anchor="w", padx=20, pady=(10, 2))

        self.txt_log = tk.Text(self, height=12, width=60, font=("Consolas", 10))
        self.txt_log.pack(padx=20, pady=(0, 15))

    def log(self, mensaje):

        self.txt_log.insert(tk.END, mensaje + "\n")
        self.txt_log.see(tk.END)

    def limpiar_log(self):
        self.txt_log.delete("1.0", tk.END)

    def prueba_excepciones(self):
        self.log("--- Ejecutando Prueba Excepciones ---")
        
        try:
            self.log("Ingresando al primer try")
            cociente = 10000 / 0
            self.log("Después de la división")
        except ZeroDivisionError:
            self.log("División por cero")
        finally:
            self.log("Ingresando al primer finally")

        try:
            self.log("Ingresando al segundo try")
            objeto = None
            objeto.to_string()
            self.log("Imprimiendo objeto")
        except ZeroDivisionError:
            self.log("División por cero")
        except Exception:
            self.log("Ocurrio una excepción")
        finally:
            self.log("Ingresando al segundo finally")
        self.log("")

    def excepcion_fuera_limite(self):
        self.log("--- Ejecutando Excepción Fuera de Límite ---")
        try:
            texto = "Programación"
            caracter = texto[14]
            self.log(str(caracter))
        except IndexError:
            self.log("Indice de string por fuera del límite")
            messagebox.showwarning("Excepción Capturada", "Indice de string por fuera del límite")
        self.log("")

    def excepcion_formato_numero(self):
        self.log("--- Ejecutando Excepción Formato Número ---")
        try:
            numero = int("Número")
            self.log(str(numero))
        except ValueError:
            self.log("Excepción de formato de número")
            messagebox.showerror("Error de Formato", "Excepción de formato de número")
        finally:
            self.log("Ingresando al finally")
        self.log("")

if __name__ == "__main__":
    app = AplicacionExcepciones()
    app.mainloop()