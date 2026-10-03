class Persona:
    def __init__(self, nombre: str, apellidos: str, numero_documento_identidad: str, anio_nacimiento: int, pais_nacimiento: str, 
        genero: str) -> None:
        
        self.nombre: str = nombre
        self.apellidos: str = apellidos
        self.numero_documento_identidad: str = numero_documento_identidad
        self.anio_nacimiento: int = anio_nacimiento
        self.pais_nacimiento: str = pais_nacimiento
        
        genero_limpio: str = genero.upper()
        if genero_limpio in ['H', 'M']:
            self.genero: str = genero_limpio
        else:
            raise ValueError("Error: El género solo puede ser 'H' (Hombre) o 'M' (Mujer).")
        
    def imprimir(self) -> None:
        print(f"Nombre = {self.nombre}")
        print(f"Apellidos = {self.apellidos}")
        print(f"Número de documento de identidad = {self.numero_documento_identidad}")
        print(f"Año de nacimiento = {self.anio_nacimiento}")
        print(f"País de nacimiento = {self.pais_nacimiento}")
        print(f"Género = {self.genero}\n")

if __name__ == "__main__":
    p1: Persona = Persona("Pedro", "Pérez", "1053121010", 1998, "Colombia", "H")
    p1.imprimir()
    
    p2: Persona = Persona("María", "Gómez", "1053223344", 2001, "México", "m")
    p2.imprimir()