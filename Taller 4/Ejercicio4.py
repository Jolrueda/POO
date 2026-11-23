import string
import tkinter as tk
from tkinter import messagebox

class ValidadorContrasena:
    @staticmethod
    def validar_contrasena(contrasena: str, confirmacion: str) -> None:
        if contrasena != confirmacion:
            raise ValueError("Las contraseñas ingresadas no coinciden.")

        caracteres_especiales = set(string.punctuation)
        
        invalida = (
            len(contrasena) < 8 or
            any(c.isspace() for c in contrasena) or
            not any(c.isalpha() for c in contrasena) or
            not any(c.isupper() for c in contrasena) or
            not any(c.isdigit() for c in contrasena) or
            not any(c in caracteres_especiales for c in contrasena)
        )

        if invalida:
            mensaje_requisitos = (
                "La contraseña ingresada no es válida. Debe cumplir obligatoriamente con todos los siguientes requisitos:\n\n"
                "• Mínimo 8 caracteres.\n"
                "• No debe tener espacios en blanco.\n"
                "• Debe tener por lo menos una letra.\n"
                "• Debe tener por lo menos una letra en mayúscula.\n"
                "• Debe tener por lo menos un número.\n"
                "• Debe tener por lo menos un carácter especial."
            )
            raise ValueError(mensaje_requisitos)


class Programador:
    def __init__(self, nombre: str, apellidos: str):
        self.nombre = nombre
        self.apellidos = apellidos


class EquipoMaratonProgramacion:
    CAPACIDAD_MAXIMA = 3

    def __init__(self, nombre_equipo: str, universidad: str, lenguaje_programacion: str, contrasena: str):
        self.nombre_equipo = nombre_equipo
        self.universidad = universidad
        self.lenguaje_programacion = lenguaje_programacion
        self.contrasena = contrasena
        self.programadores: list[Programador] = []

    @property
    def tamano_equipo(self) -> int:
        return len(self.programadores)

    def esta_lleno(self) -> bool:
        return len(self.programadores) >= self.CAPACIDAD_MAXIMA

    def anadir(self, programador: Programador) -> None:
        if self.esta_lleno():
            raise Exception("El equipo está completo. No se pudo agregar programador.")

        self.programadores.append(programador)

    @staticmethod
    def validar_campo(campo: str) -> None:
        if not campo.strip():
            raise ValueError("Los campos de nombre/apellido no pueden estar vacíos.")
            
        if any(c.isdigit() for c in campo):
            raise Exception(f"El texto '{campo}' no puede tener dígitos.")

        if len(campo) > 20:
            raise Exception(f"La longitud de '{campo}' no debe ser superior a 20 caracteres.")


class InterfazRegistroMaraton(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Registro - Maratón de Programación")
        self.geometry("450x650")
        self.resizable(False, False)

        self.var_equipo = tk.StringVar()
        self.var_universidad = tk.StringVar()
        self.var_lenguaje = tk.StringVar()
        self.var_contrasena = tk.StringVar()
        self.var_confirmacion = tk.StringVar()

        self.vars_nombres = [tk.StringVar() for _ in range(EquipoMaratonProgramacion.CAPACIDAD_MAXIMA)]
        self.vars_apellidos = [tk.StringVar() for _ in range(EquipoMaratonProgramacion.CAPACIDAD_MAXIMA)]

        self.crear_widgets()

    def crear_widgets(self):
        frame_equipo = tk.LabelFrame(self, text="1. Datos del Equipo", padx=10, pady=10)
        frame_equipo.pack(fill="x", padx=15, pady=10)

        tk.Label(frame_equipo, text="Nombre del Equipo:").grid(row=0, column=0, sticky="e", pady=2)
        tk.Entry(frame_equipo, textvariable=self.var_equipo, width=30).grid(row=0, column=1, padx=5, pady=2)

        tk.Label(frame_equipo, text="Universidad:").grid(row=1, column=0, sticky="e", pady=2)
        tk.Entry(frame_equipo, textvariable=self.var_universidad, width=30).grid(row=1, column=1, padx=5, pady=2)

        tk.Label(frame_equipo, text="Lenguaje:").grid(row=2, column=0, sticky="e", pady=2)
        tk.Entry(frame_equipo, textvariable=self.var_lenguaje, width=30).grid(row=2, column=1, padx=5, pady=2)

        tk.Label(frame_equipo, text="Contraseña:").grid(row=3, column=0, sticky="e", pady=2)
        tk.Entry(frame_equipo, textvariable=self.var_contrasena, show="*", width=30).grid(row=3, column=1, padx=5, pady=2)

        tk.Label(frame_equipo, text="Confirmar Contraseña:").grid(row=4, column=0, sticky="e", pady=2)
        tk.Entry(frame_equipo, textvariable=self.var_confirmacion, show="*", width=30).grid(row=4, column=1, padx=5, pady=2)

        frame_integrantes = tk.LabelFrame(self, text="2. Datos de los Integrantes", padx=10, pady=10)
        frame_integrantes.pack(fill="x", padx=15, pady=5)

        for i in range(EquipoMaratonProgramacion.CAPACIDAD_MAXIMA):
            tk.Label(frame_integrantes, text=f"--- Integrante {i+1} ---", fg="gray").grid(row=i*3, column=0, columnspan=2, pady=(10, 0))

            tk.Label(frame_integrantes, text="Nombre(s):").grid(row=i*3+1, column=0, sticky="e", pady=2)
            tk.Entry(frame_integrantes, textvariable=self.vars_nombres[i], width=30).grid(row=i*3+1, column=1, padx=5, pady=2)

            tk.Label(frame_integrantes, text="Apellidos:").grid(row=i*3+2, column=0, sticky="e", pady=2)
            tk.Entry(frame_integrantes, textvariable=self.vars_apellidos[i], width=30).grid(row=i*3+2, column=1, padx=5, pady=2)

        btn_registrar = tk.Button(self, text="Validar y Registrar Equipo", bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), command=self.registrar)
        btn_registrar.pack(pady=20)

    def registrar(self):
        try:
            if not self.var_equipo.get() or not self.var_universidad.get() or not self.var_lenguaje.get():
                raise ValueError("Los datos del equipo (Nombre, Universidad, Lenguaje) no pueden estar vacíos.")

            ValidadorContrasena.validar_contrasena(self.var_contrasena.get(), self.var_confirmacion.get())

            equipo = EquipoMaratonProgramacion(
                self.var_equipo.get(),
                self.var_universidad.get(),
                self.var_lenguaje.get(),
                self.var_contrasena.get()
            )

            for i in range(EquipoMaratonProgramacion.CAPACIDAD_MAXIMA):
                nombre_prog = self.vars_nombres[i].get()
                apellido_prog = self.vars_apellidos[i].get()

                EquipoMaratonProgramacion.validar_campo(nombre_prog)
                EquipoMaratonProgramacion.validar_campo(apellido_prog)

                programador = Programador(nombre_prog, apellido_prog)
                equipo.anadir(programador)

            mensaje = f"¡Equipo '{equipo.nombre_equipo}' de la universidad '{equipo.universidad}' registrado exitosamente con {equipo.tamano_equipo} integrantes!"
            messagebox.showinfo("Registro Exitoso", mensaje)

        except (ValueError, Exception) as error:
            messagebox.showerror("Error de Validación", str(error))


if __name__ == "__main__":
    app = InterfazRegistroMaraton()
    app.mainloop()