import tkinter as tk
from tkinter import filedialog, messagebox

def leer_archivo_original():
    nombre_archivo = entrada_ruta.get().strip()
    
    if not nombre_archivo:
        messagebox.showwarning("Advertencia", "Por favor, ingrese la ruta del archivo.")
        return

    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
            
            caja_texto.delete("1.0", tk.END)
            caja_texto.insert(tk.END, "--- Contenido original ---\n\n")
            caja_texto.insert(tk.END, contenido)

    except IOError:
        messagebox.showerror("Error", "No se pudo leer el archivo.\nVerifique que la ruta sea correcta y el archivo exista.")


def mostrar_en_mayusculas():
    nombre_archivo = entrada_ruta.get().strip()
    
    if not nombre_archivo:
        messagebox.showwarning("Advertencia", "Por favor, ingrese la ruta del archivo.")
        return
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            contenido = archivo.read()            
            contenido_mayusculas = contenido.upper()
            
            caja_texto.delete("1.0", tk.END)
            caja_texto.insert(tk.END, "--- Contenido en mayúsculas ---\n\n")
            caja_texto.insert(tk.END, contenido_mayusculas)

    except IOError:
        messagebox.showerror("Error", "No se pudo leer el archivo.\nVerifique que la ruta sea correcta y el archivo exista.")

def examinar_archivo():
    ruta = filedialog.askopenfilename(
        title="Seleccionar archivo de texto",
        filetypes=(("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*"))
    )
    if ruta: 
        entrada_ruta.delete(0, tk.END)
        entrada_ruta.insert(0, ruta)

ventana = tk.Tk()
ventana.title("Lector de Archivos .txt")
ventana.geometry("600x500")
ventana.config(padx=20, pady=20)

label_instruccion = tk.Label(ventana, text="Ruta del archivo de texto:", font=("Arial", 10, "bold"))
label_instruccion.pack(anchor="w")

frame_ruta = tk.Frame(ventana)
frame_ruta.pack(fill="x", pady=5)

entrada_ruta = tk.Entry(frame_ruta, width=50, font=("Arial", 10))
entrada_ruta.pack(side="left", fill="x", expand=True, padx=(0, 10))

boton_examinar = tk.Button(frame_ruta, text="Examinar...", command=examinar_archivo)
boton_examinar.pack(side="right")

frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=15)

boton_original = tk.Button(frame_botones, text="Mostrar Original", command=leer_archivo_original, width=20, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"))
boton_original.pack(side="left", padx=10)

boton_mayusculas = tk.Button(frame_botones, text="Mostrar en Mayúsculas", command=mostrar_en_mayusculas, width=20, bg="#2196F3", fg="white", font=("Arial", 10, "bold"))
boton_mayusculas.pack(side="right", padx=10)

frame_texto = tk.Frame(ventana)
frame_texto.pack(fill="both", expand=True)

scrollbar = tk.Scrollbar(frame_texto)
scrollbar.pack(side="right", fill="y")

caja_texto = tk.Text(frame_texto, height=15, width=60, font=("Courier", 10), yscrollcommand=scrollbar.set)
caja_texto.pack(side="left", fill="both", expand=True)

scrollbar.config(command=caja_texto.yview)

ventana.mainloop()