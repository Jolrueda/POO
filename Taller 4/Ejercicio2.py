import tkinter as tk
from tkinter import ttk, messagebox

class Vendedor:
    """Modela un vendedor y valida su edad."""
    def __init__(self, nombre: str, apellidos: str):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = 0

    def verificar_edad(self, edad: int):
        if edad < 18:
            raise ValueError("El vendedor debe ser mayor de 18 años.")
        if 0 <= edad < 120:
            self.edad = edad
        else:
            raise ValueError("La edad no puede ser negativa ni mayor a 120.")


class ObjetoConExcepcion:
    """Clase cuyo constructor valida los datos y lanza una excepción si es inválido."""
    def __init__(self, parametro: str):
        if not parametro or parametro.strip() == "":
            raise ValueError("[Excepción en Constructor]: El parámetro no puede estar vacío.")
        if parametro.lower() == "error":
            raise RuntimeError("[Excepción en Constructor]: Se forzó un error crítico al instanciar.")
        self.parametro = parametro


class TablaASCII:
    """Modela una tabla ASCII con métodos get y set gestionando excepciones."""
    def __init__(self):
        self.tabla = {chr(i): i for i in range(128)}

    def get(self, simbolo: str) -> int:
        if len(simbolo) != 1:
            raise ValueError("El símbolo debe ser exactamente un único carácter.")
        if simbolo in self.tabla:
            return self.tabla[simbolo]
        else:
            raise KeyError(f"El símbolo '{simbolo}' no existe en la tabla ASCII.")

    def set(self, simbolo: str, numero: int):
        if len(simbolo) != 1:
            raise ValueError("El símbolo debe ser exactamente un único carácter.")
        if not (0 <= numero <= 255):
            raise ValueError("El número ASCII debe estar en el rango de 0 a 255.")
        self.tabla[simbolo] = numero


class AplicacionTaller(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Taller 4 - Excepciones y POO")
        self.geometry("640x500")
        self.resizable(False, False)
        
        self.COLOR_BG = "#F4F6F7"
        self.COLOR_PRIMARIO = "#2C3E50"
        self.COLOR_BOTON = "#2980B9"
        self.configure(bg=self.COLOR_BG)

        self.tabla_ascii = TablaASCII()

        label_titulo = tk.Label(
            self,
            text="Taller de Excepciones en Python",
            font=("Helvetica", 15, "bold"),
            bg=self.COLOR_BG,
            fg=self.COLOR_PRIMARIO,
        )
        label_titulo.pack(pady=10)

        notebook = ttk.Notebook(self)
        notebook.pack(padx=15, pady=5, fill="both", expand=True)

        tab_vendedor = tk.Frame(notebook, bg=self.COLOR_BG)
        tab_constructor = tk.Frame(notebook, bg=self.COLOR_BG)
        tab_ascii = tk.Frame(notebook, bg=self.COLOR_BG)

        notebook.add(tab_vendedor, text="1. Vendedor")
        notebook.add(tab_constructor, text="2. Excepción Constructor")
        notebook.add(tab_ascii, text="3. Tabla ASCII")

        self._setup_tab_vendedor(tab_vendedor)
        self._setup_tab_constructor(tab_constructor)
        self._setup_tab_ascii(tab_ascii)

        label_consola = tk.Label(
            self,
            text="Consola de Salida / Captura de Excepciones:",
            font=("Helvetica", 10, "bold"),
            bg=self.COLOR_BG,
            fg=self.COLOR_PRIMARIO,
        )
        label_consola.pack(anchor="w", padx=20, pady=(10, 2))

        self.txt_log = tk.Text(
            self, height=9, width=74, font=("Consolas", 9), bg="#1E1E1E", fg="#00FF00"
        )
        self.txt_log.pack(padx=20, pady=(0, 15))

    def log(self, mensaje: str):
        self.txt_log.insert(tk.END, mensaje + "\n")
        self.txt_log.see(tk.END)

    def _setup_tab_vendedor(self, parent):
        frame = tk.LabelFrame(parent, text=" Datos del Vendedor ", bg=self.COLOR_BG, fg=self.COLOR_PRIMARIO, padx=15, pady=10)
        frame.pack(padx=15, pady=15, fill="x")

        tk.Label(frame, text="Nombre:", bg=self.COLOR_BG).grid(row=0, column=0, sticky="w", pady=4)
        self.ent_v_nom = ttk.Entry(frame, width=30)
        self.ent_v_nom.grid(row=0, column=1, pady=4, padx=5)

        tk.Label(frame, text="Apellidos:", bg=self.COLOR_BG).grid(row=1, column=0, sticky="w", pady=4)
        self.ent_v_ape = ttk.Entry(frame, width=30)
        self.ent_v_ape.grid(row=1, column=1, pady=4, padx=5)

        tk.Label(frame, text="Edad:", bg=self.COLOR_BG).grid(row=2, column=0, sticky="w", pady=4)
        self.ent_v_edad = ttk.Entry(frame, width=30)
        self.ent_v_edad.grid(row=2, column=1, pady=4, padx=5)

        btn = tk.Button(parent, text="Validar y Registrar Vendedor", bg=self.COLOR_BOTON, fg="white", font=("Helvetica", 9, "bold"), command=self._validar_vendedor)
        btn.pack(pady=10)

    def _validar_vendedor(self):
        try:
            nom = self.ent_v_nom.get().strip()
            ape = self.ent_v_ape.get().strip()
            edad_str = self.ent_v_edad.get().strip()

            if not nom or not ape or not edad_str:
                raise ValueError("Todos los campos son obligatorios.")

            edad = int(edad_str)
            v = Vendedor(nom, ape)
            v.verificar_edad(edad)

            self.log(f"[ÉXITO VENDEDOR]: {v.nombre} {v.apellidos} registrado con {v.edad} años.")
            messagebox.showinfo("Éxito", f"Vendedor {v.nombre} {v.apellidos} registrado correctamente.")

        except ValueError as e:
            msg = str(e) if "invalid literal" not in str(e) else "La edad debe ser un número entero."
            self.log(f"[EXCEPCIÓN CAPTURADA]: {msg}")
            messagebox.showerror("Error de Excepción", msg)
   
    def _setup_tab_constructor(self, parent):
        frame = tk.LabelFrame(parent, text=" Probar Excepción desde __init__ ", bg=self.COLOR_BG, fg=self.COLOR_PRIMARIO, padx=15, pady=10)
        frame.pack(padx=15, pady=15, fill="x")

        tk.Label(frame, text="Parámetro (déjalo vacío o escribe 'error' para provocar la excepción):", bg=self.COLOR_BG).pack(anchor="w", pady=4)
        self.ent_param = ttk.Entry(frame, width=45)
        self.ent_param.pack(pady=4)

        btn = tk.Button(parent, text="Crear Objeto (Instanciar)", bg=self.COLOR_BOTON, fg="white", font=("Helvetica", 9, "bold"), command=self._crear_objeto_constructor)
        btn.pack(pady=10)

    def _crear_objeto_constructor(self):
        self.log("--- Intentando instanciar ObjetoConExcepcion ---")
        try:
            param = self.ent_param.get()
            obj = ObjetoConExcepcion(param)
            self.log(f"[ÉXITO]: Objeto instanciado con parámetro: '{obj.parametro}'")
            messagebox.showinfo("Éxito", "Objeto creado correctamente sin errores.")
        except (ValueError, RuntimeError) as e:
            self.log(f"[CAPTURADO DESDE CONSTRUCTOR]: {e}")
            messagebox.showerror("Excepción en Constructor", str(e))

    def _setup_tab_ascii(self, parent):
        frame_set = tk.LabelFrame(parent, text=" Método set(símbolo, número) ", bg=self.COLOR_BG, fg=self.COLOR_PRIMARIO, padx=10, pady=8)
        frame_set.pack(padx=15, pady=10, fill="x")

        tk.Label(frame_set, text="Símbolo:", bg=self.COLOR_BG).grid(row=0, column=0)
        self.ent_ascii_sim_set = ttk.Entry(frame_set, width=6)
        self.ent_ascii_sim_set.grid(row=0, column=1, padx=5)

        tk.Label(frame_set, text="Número (0-255):", bg=self.COLOR_BG).grid(row=0, column=2)
        self.ent_ascii_num_set = ttk.Entry(frame_set, width=6)
        self.ent_ascii_num_set.grid(row=0, column=3, padx=5)

        btn_set = tk.Button(frame_set, text="Asociar (Set)", bg=self.COLOR_BOTON, fg="white", command=self._ascii_set)
        btn_set.grid(row=0, column=4, padx=10)

        frame_get = tk.LabelFrame(parent, text=" Método get(símbolo) ", bg=self.COLOR_BG, fg=self.COLOR_PRIMARIO, padx=10, pady=8)
        frame_get.pack(padx=15, pady=10, fill="x")

        tk.Label(frame_get, text="Símbolo:", bg=self.COLOR_BG).grid(row=0, column=0)
        self.ent_ascii_sim_get = ttk.Entry(frame_get, width=6)
        self.ent_ascii_sim_get.grid(row=0, column=1, padx=5)

        btn_get = tk.Button(frame_get, text="Obtener (Get)", bg=self.COLOR_BOTON, fg="white", command=self._ascii_get)
        btn_get.grid(row=0, column=2, padx=10)

    def _ascii_set(self):
        try:
            simbolo = self.ent_ascii_sim_set.get()
            num_str = self.ent_ascii_num_set.get().strip()
            if not num_str:
                raise ValueError("Debe ingresar un número entero.")
            
            numero = int(num_str)
            self.tabla_ascii.set(simbolo, numero)
            self.log(f"[ASCII SET]: Símbolo '{simbolo}' asociado al valor {numero}.")
            messagebox.showinfo("Éxito", f"Símbolo '{simbolo}' asignado correctamente a {numero}.")
        except (ValueError, TypeError) as e:
            msg = str(e) if "invalid literal" not in str(e) else "El valor debe ser un número entero."
            self.log(f"[ERROR ASCII SET]: {msg}")
            messagebox.showerror("Error en Set", msg)

    def _ascii_get(self):
        try:
            simbolo = self.ent_ascii_sim_get.get()
            valor = self.tabla_ascii.get(simbolo)
            self.log(f"[ASCII GET]: El símbolo '{simbolo}' tiene el valor ASCII: {valor}.")
            messagebox.showinfo("Resultado GET", f"Símbolo: '{simbolo}' -> Valor: {valor}")
        except (ValueError, KeyError) as e:
            self.log(f"[ERROR ASCII GET]: {e}")
            messagebox.showerror("Error en Get", str(e))

if __name__ == "__main__":
    app = AplicacionTaller()
    app.mainloop()