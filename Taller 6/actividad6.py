import os
import tkinter as tk
from tkinter import messagebox

class Contacto:
  def __init__(self, nombre: str, numero: str):
    self.nombre = nombre.strip()
    self.numero = numero.strip()

  def a_formato_archivo(self) -> str:
    return f"{self.nombre}!{self.numero}\n"

  @staticmethod
  def desde_linea(linea: str):
    partes = linea.strip().split("!")
    if len(partes) == 2:
      return Contacto(partes[0], partes[1])
    return None


class GestorArchivos:
  def __init__(self, ruta_archivo: str = "friendsContact.txt"):
    self.ruta_archivo = ruta_archivo
    self._verificar_archivo()

  def _verificar_archivo(self):
    if not os.path.exists(self.ruta_archivo):
      with open(self.ruta_archivo, "w", encoding="utf-8") as archivo:
        pass

  def crear(self, nuevo_contacto: Contacto) -> tuple[bool, str]:
    contactos = self.leer_todos()

    for c in contactos:
      if (
          c.nombre.lower() == nuevo_contacto.nombre.lower()
          or c.numero == nuevo_contacto.numero
      ):
        return False, "El nombre o número de contacto ya existe."

    with open(self.ruta_archivo, "a", encoding="utf-8") as archivo:
      archivo.write(nuevo_contacto.a_formato_archivo())

    return True, "Contacto agregado exitosamente."

  def leer_todos(self) -> list[Contacto]:
    self._verificar_archivo()
    contactos = []
    with open(self.ruta_archivo, "r", encoding="utf-8") as archivo:
      for linea in archivo:
        if linea.strip():
          contacto = Contacto.desde_linea(linea)
          if contacto:
            contactos.append(contacto)
    return contactos

  def buscar_por_nombre(self, nombre: str) -> Contacto | None:
    for c in self.leer_todos():
      if c.nombre.lower() == nombre.strip().lower():
        return c
    return None

  def actualizar(self, nombre: str, nuevo_numero: str) -> tuple[bool, str]:
    contactos = self.leer_todos()
    encontrado = False
    ruta_temp = "temp.txt"

    with open(ruta_temp, "w", encoding="utf-8") as archivo_temp:
      for c in contactos:
        if c.nombre.lower() == nombre.strip().lower():
          c.numero = nuevo_numero.strip()
          encontrado = True
        archivo_temp.write(c.a_formato_archivo())

    if encontrado:
      os.replace(ruta_temp, self.ruta_archivo)
      return True, "Contacto actualizado correctamente."
    else:
      if os.path.exists(ruta_temp):
        os.remove(ruta_temp)
      return False, "El nombre ingresado no existe."

  def eliminar(self, nombre: str) -> tuple[bool, str]:
    contactos = self.leer_todos()
    encontrado = False
    ruta_temp = "temp.txt"

    with open(ruta_temp, "w", encoding="utf-8") as archivo_temp:
      for c in contactos:
        if c.nombre.lower() == nombre.strip().lower():
          encontrado = True
          continue  
        archivo_temp.write(c.a_formato_archivo())

    if encontrado:
      os.replace(ruta_temp, self.ruta_archivo)
      return True, "Contacto eliminado correctamente."
    else:
      if os.path.exists(ruta_temp):
        os.remove(ruta_temp)
      return False, "El nombre ingresado no existe."


class InterfazContactos:
  def __init__(self, root: tk.Tk):
    self.root = root
    self.root.title("Gestión de Contactos - POO Actividad 6")
    self.root.geometry("450x420")
    self.root.resizable(False, False)

    self.gestor = GestorArchivos("friendsContact.txt")
    self._construir_interfaz()
    self.accion_read()

  def _construir_interfaz(self):
    lbl_titulo = tk.Label(
        self.root,
        text="Directorio de Amigos (CRUD)",
        font=("Arial", 14, "bold"),
    )
    lbl_titulo.pack(pady=10)

    frame_form = tk.Frame(self.root)
    frame_form.pack(pady=5, padx=20, fill="x")

    tk.Label(frame_form, text="Nombre:", font=("Arial", 10)).grid(
        row=0, column=0, sticky="w", pady=5
    )
    self.entry_nombre = tk.Entry(frame_form, width=32, font=("Arial", 10))
    self.entry_nombre.grid(row=0, column=1, pady=5, padx=10)

    tk.Label(frame_form, text="Número:", font=("Arial", 10)).grid(
        row=1, column=0, sticky="w", pady=5
    )
    self.entry_numero = tk.Entry(frame_form, width=32, font=("Arial", 10))
    self.entry_numero.grid(row=1, column=1, pady=5, padx=10)

    frame_botones = tk.Frame(self.root)
    frame_botones.pack(pady=10)

    btn_create = tk.Button(
        frame_botones,
        text="Create",
        width=9,
        bg="#4CAF50",
        fg="white",
        font=("Arial", 9, "bold"),
        command=self.accion_create,
    )
    btn_create.grid(row=0, column=0, padx=5)

    btn_read = tk.Button(
        frame_botones,
        text="Read",
        width=9,
        bg="#2196F3",
        fg="white",
        font=("Arial", 9, "bold"),
        command=self.accion_read,
    )
    btn_read.grid(row=0, column=1, padx=5)

    btn_update = tk.Button(
        frame_botones,
        text="Update",
        width=9,
        bg="#FF9800",
        fg="white",
        font=("Arial", 9, "bold"),
        command=self.accion_update,
    )
    btn_update.grid(row=0, column=2, padx=5)

    btn_delete = tk.Button(
        frame_botones,
        text="Delete",
        width=9,
        bg="#F44336",
        fg="white",
        font=("Arial", 9, "bold"),
        command=self.accion_delete,
    )
    btn_delete.grid(row=0, column=3, padx=5)

    btn_limpiar = tk.Button(
        frame_botones,
        text="Limpiar",
        width=8,
        font=("Arial", 9),
        command=self.limpiar_campos,
    )
    btn_limpiar.grid(row=0, column=4, padx=5)

    tk.Label(
        self.root,
        text="Registros en friendsContact.txt:",
        font=("Arial", 10, "bold"),
    ).pack(pady=(10, 2))

    self.lista_contactos = tk.Listbox(
        self.root, width=55, height=11, font=("Consolas", 10)
    )
    self.lista_contactos.pack(pady=5, padx=20)
    self.lista_contactos.bind("<<ListboxSelect>>", self.seleccionar_contacto)

  def _validar_numero(self, numero: str) -> bool:
    return numero.isdigit()

  def limpiar_campos(self):
    self.entry_nombre.delete(0, tk.END)
    self.entry_numero.delete(0, tk.END)

  def seleccionar_contacto(self, event):
    seleccion = self.lista_contactos.curselection()
    if seleccion:
      texto = self.lista_contactos.get(seleccion[0])
      if " - " in texto:
        nombre, numero = texto.split(" - ")
        self.limpiar_campos()
        self.entry_nombre.insert(0, nombre.strip())
        self.entry_numero.insert(0, numero.strip())

  def accion_create(self):
    nombre = self.entry_nombre.get().strip()
    numero = self.entry_numero.get().strip()

    if not nombre or not numero:
      messagebox.showwarning(
          "Campos vacíos", "Por favor ingresa el nombre y el número."
      )
      return

    if not self._validar_numero(numero):
      messagebox.showerror(
          "Error de formato", "El número de contacto debe ser numérico."
      )
      return

    contacto = Contacto(nombre, numero)
    exito, mensaje = self.gestor.crear(contacto)

    if exito:
      messagebox.showinfo("Éxito", mensaje)
      self.limpiar_campos()
      self.accion_read()
    else:
      messagebox.showwarning("Aviso", mensaje)

  def accion_read(self):
    nombre_busqueda = self.entry_nombre.get().strip()
    self.lista_contactos.delete(0, tk.END)

    if nombre_busqueda:
      contacto = self.gestor.buscar_por_nombre(nombre_busqueda)
      if contacto:
        self.entry_numero.delete(0, tk.END)
        self.entry_numero.insert(0, contacto.numero)
        self.lista_contactos.insert(
            tk.END, f"{contacto.nombre} - {contacto.numero}"
        )
      else:
        messagebox.showinfo("Búsqueda", "El nombre ingresado no existe.")
    else:
      contactos = self.gestor.leer_todos()
      for c in contactos:
        self.lista_contactos.insert(tk.END, f"{c.nombre} - {c.numero}")

  def accion_update(self):
    nombre = self.entry_nombre.get().strip()
    nuevo_numero = self.entry_numero.get().strip()

    if not nombre or not nuevo_numero:
      messagebox.showwarning(
          "Campos vacíos",
          "Ingresa el nombre a actualizar y su nuevo número.",
      )
      return

    if not self._validar_numero(nuevo_numero):
      messagebox.showerror(
          "Error de formato", "El número de contacto debe ser numérico."
      )
      return

    exito, mensaje = self.gestor.actualizar(nombre, nuevo_numero)
    if exito:
      messagebox.showinfo("Éxito", mensaje)
      self.limpiar_campos()
      self.accion_read()
    else:
      messagebox.showwarning("Aviso", mensaje)

  def accion_delete(self):
    nombre = self.entry_nombre.get().strip()

    if not nombre:
      messagebox.showwarning(
          "Campo vacío", "Ingresa o selecciona el nombre del contacto a eliminar."
      )
      return

    exito, mensaje = self.gestor.eliminar(nombre)
    if exito:
      messagebox.showinfo("Éxito", mensaje)
      self.limpiar_campos()
      self.accion_read()
    else:
      messagebox.showwarning("Aviso", mensaje)

if __name__ == "__main__":
  ventana = tk.Tk()
  app = InterfazContactos(ventana)
  ventana.mainloop()