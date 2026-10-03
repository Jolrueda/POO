from enum import Enum

class TipoCombustible(Enum):
    GASOLINA = "Gasolina"
    BIOETANOL = "Bioetanol"
    DIESEL = "Diésel"
    BIODIESEL = "Biodiésel"
    GAS_NATURAL = "Gas natural"

class TipoAutomovil(Enum):
    CARRO_DE_CIUDAD = "Carro de ciudad"
    SUBCOMPACTO = "Subcompacto"
    COMPACTO = "Compacto"
    FAMILIAR = "Familiar"
    EJECUTIVO = "Ejecutivo"
    SUV = "SUV"

class Color(Enum):
    BLANCO = "Blanco"
    NEGRO = "Negro"
    ROJO = "Rojo"
    NARANJA = "Naranja"
    AMARILLO = "Amarillo"
    VERDE = "Verde"
    AZUL = "Azul"
    VIOLETA = "Violeta"

class Automovil:
    def __init__(self, marca: str, modelo: int, motor: float, tipo_combustible: TipoCombustible, tipo_automovil: TipoAutomovil, numero_puertas: int, cantidad_asientos: int, velocidad_maxima: int, color: Color, es_automatico: bool, velocidad_actual: int = 0) -> None:
        self.marca: str = marca
        self.modelo: int = modelo
        self.motor: float = motor
        self.tipo_combustible: TipoCombustible = tipo_combustible
        self.tipo_automovil: TipoAutomovil = tipo_automovil
        self.numero_puertas: int = numero_puertas
        self.cantidad_asientos: int = cantidad_asientos
        self.velocidad_maxima: int = velocidad_maxima
        self.color: Color = color
        self.es_automatico: bool = es_automatico
        self.velocidad_actual: int = velocidad_actual
        self.total_multas: float = 0.0

    def get_marca(self) -> str:
        return self.marca

    def set_marca(self, marca: str) -> None:
        self.marca = marca

    def get_modelo(self) -> int:
        return self.modelo

    def set_modelo(self, modelo: int) -> None:
        self.modelo = modelo

    def get_motor(self) -> float:
        return self.motor

    def set_motor(self, motor: float) -> None:
        self.motor = motor

    def get_tipo_combustible(self) -> TipoCombustible:
        return self.tipo_combustible

    def set_tipo_combustible(self, tipo_combustible: TipoCombustible) -> None:
        self.tipo_combustible = tipo_combustible

    def get_tipo_automovil(self) -> TipoAutomovil:
        return self.tipo_automovil

    def set_tipo_automovil(self, tipo_automovil: TipoAutomovil) -> None:
        self.tipo_automovil = tipo_automovil

    def get_numero_puertas(self) -> int:
        return self.numero_puertas

    def set_numero_puertas(self, numero_puertas: int) -> None:
        self.numero_puertas = numero_puertas

    def get_cantidad_asientos(self) -> int:
        return self.cantidad_asientos

    def set_cantidad_asientos(self, cantidad_asientos: int) -> None:
        self.cantidad_asientos = cantidad_asientos

    def get_velocidad_maxima(self) -> int:
        return self.velocidad_maxima

    def set_velocidad_maxima(self, velocidad_maxima: int) -> None:
        self.velocidad_maxima = velocidad_maxima

    def get_color(self) -> Color:
        return self.color

    def set_color(self, color: Color) -> None:
        self.color = color

    def get_es_automatico(self) -> bool:
        return self.es_automatico

    def set_es_automatico(self, es_automatico: bool) -> None:
        self.es_automatico = es_automatico

    def get_velocidad_actual(self) -> int:
        return self.velocidad_actual

    def set_velocidad_actual(self, velocidad_actual: int) -> None:
        if 0 <= velocidad_actual <= self.velocidad_maxima:
            self.velocidad_actual = velocidad_actual
        else:
            print("No es posible asignar esa velocidad actual.")

    def acelerar(self, incremento: int) -> None:
        if self.velocidad_actual + incremento > self.velocidad_maxima:
            print("Multa generada: Se intentó superar la velocidad máxima permitida.")
            self.total_multas += 100000.0 
        else:
            self.velocidad_actual += incremento

    def desacelerar(self, decremento: int) -> None:
        if self.velocidad_actual - decremento < 0:
            print("No se puede desacelerar a una velocidad negativa.")
        else:
            self.velocidad_actual -= decremento

    def frenar(self) -> None:
        self.velocidad_actual = 0

    def calcular_tiempo_llegada(self, distancia: float) -> float:
        if self.velocidad_actual > 0:
            return distancia / self.velocidad_actual
        print("El automóvil está detenido, no se puede calcular el tiempo de llegada.")
        return 0.0

    def tiene_multas(self) -> bool:
        return self.total_multas > 0

    def valor_total_multas(self) -> float:
        return self.total_multas

    def imprimir(self) -> None:
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Motor: {self.motor} L")
        print(f"Tipo de combustible: {self.tipo_combustible.value}")
        print(f"Tipo de automóvil: {self.tipo_automovil.value}")
        print(f"Número de puertas: {self.numero_puertas}")
        print(f"Cantidad de asientos: {self.cantidad_asientos}")
        print(f"Velocidad máxima: {self.velocidad_maxima} km/h")
        print(f"Color: {self.color.value}")
        print(f"Es automático: {'Sí' if self.es_automatico else 'No'}")
        print(f"Velocidad actual: {self.velocidad_actual} km/h")
        print(f"Tiene multas: {'Sí' if self.tiene_multas() else 'No'}")
        print(f"Valor total multas: ${self.valor_total_multas()}\n")


if __name__ == "__main__":
    auto = Automovil("Ford", 2018, 3.0, TipoCombustible.GASOLINA, TipoAutomovil.EJECUTIVO, 5, 6, 250, Color.NEGRO, True)
    
    auto.imprimir()

    auto.set_velocidad_actual(100)
    print(f"Velocidad actual: {auto.get_velocidad_actual()} km/h")

    auto.acelerar(20)
    print(f"Velocidad actual: {auto.get_velocidad_actual()} km/h")

    auto.desacelerar(50)
    print(f"Velocidad actual: {auto.get_velocidad_actual()} km/h")

    auto.acelerar(200) 
    auto.acelerar(100) 
    
    print(f"¿Tiene multas?: {'Sí' if auto.tiene_multas() else 'No'}")
    print(f"Valor total a pagar por multas: ${auto.valor_total_multas()}")

    auto.frenar()
    print(f"Velocidad actual: {auto.get_velocidad_actual()} km/h")