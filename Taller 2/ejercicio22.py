from enum import Enum

class TipoPlaneta(Enum):
    GASEOSO = 1
    TERRESTRE = 2
    ENANO = 3

class Planeta:
    def __init__(self, nombre: str, cantidad_satelites: int, masa: float, volumen: float, diametro: float, distancia_sol: float, tipo: TipoPlaneta, es_observable: bool, periodo_orbital: float, periodo_rotacion: float) -> None:
        self.nombre: str = nombre
        self.cantidad_satelites: int = cantidad_satelites
        self.masa: float = masa                    
        self.volumen: float = volumen              
        self.diametro: float = diametro            
        self.distancia_sol: float = distancia_sol  
        self.tipo: TipoPlaneta = tipo                    
        self.es_observable: bool = es_observable  
        self.periodo_orbital: float = periodo_orbital
        self.periodo_rotacion: float = periodo_rotacion

    def imprimir(self) -> None:
        print(f"Nombre: {self.nombre}")
        print(f"Cantidad de satélites: {self.cantidad_satelites}")
        print(f"Masa: {self.masa} kg")
        print(f"Volumen: {self.volumen} km³")
        print(f"Diámetro: {self.diametro} km")
        print(f"Distancia al Sol: {self.distancia_sol} millones de km")
        print(f"Tipo de planeta: {self.tipo.name}") 
        print(f"Es observable a simple vista: {'Sí' if self.es_observable else 'No'}")
        print(f"Periodo orbital: {self.periodo_orbital} años")
        print(f"Periodo de rotación: {self.periodo_rotacion} días")

    def calcular_densidad(self) -> float:
        if self.volumen != 0:
            return self.masa / self.volumen
        return 0.0

    def es_planeta_exterior(self) -> bool:
        limite_exterior: float = 500.0
        return self.distancia_sol > limite_exterior


if __name__ == "__main__":
    p1 = Planeta(nombre="Tierra", cantidad_satelites=1, masa=5.9736e24, volumen=1.08321e12, diametro=12742.0, distancia_sol=150.0, tipo=TipoPlaneta.TERRESTRE, es_observable=True, periodo_orbital=1.0, periodo_rotacion=1.0)
    
    p2 = Planeta(nombre="Júpiter", cantidad_satelites=79, masa=1.899e27, volumen=1.43128e15, diametro=139820.0, distancia_sol=778.0, tipo=TipoPlaneta.GASEOSO, es_observable=True, periodo_orbital=11.86, periodo_rotacion=0.41)

    print("--- Datos del Planeta 1 ---")
    p1.imprimir()
    print(f"Densidad: {p1.calcular_densidad():.2e} kg/km³")
    print(f"¿Es planeta exterior?: {'Sí' if p1.es_planeta_exterior() else 'No'}\n")

    print("--- Datos del Planeta 2 ---")
    p2.imprimir()
    print(f"Densidad: {p2.calcular_densidad():.2e} kg/km³")
    print(f"¿Es planeta exterior?: {'Sí' if p2.es_planeta_exterior() else 'No'}")