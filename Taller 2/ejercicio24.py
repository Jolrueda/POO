import math

class Circulo:
    def __init__(self, radio: float) -> None:
        self.radio: float = radio

    def area(self) -> float:
        return 3.14159 * (self.radio**2)

    def perimetro(self) -> float:
        return 2 * 3.14159 * self.radio


class Rectangulo:
    def __init__(self, base: float, altura: float) -> None:
        self.base: float = base
        self.altura: float = altura

    def area(self) -> float:
        return self.base * self.altura

    def perimetro(self) -> float:
        return 2 * (self.base + self.altura)


class Cuadrado:
    def __init__(self, lado: float) -> None:
        self.lado: float = lado

    def area(self) -> float:
        return self.lado**2

    def perimetro(self) -> float:
        return 4 * self.lado


class TrianguloRectangulo:
    def __init__(self, base: float, altura: float) -> None:
        self.base: float = base
        self.altura: float = altura

    def area(self) -> float:
        return (self.base * self.altura) / 2

    def calcular_hipotenusa(self) -> float:
        return (self.base**2 + self.altura**2) ** 0.5

    def perimetro(self) -> float:
        hipotenusa: float = self.calcular_hipotenusa()
        return self.base + self.altura + hipotenusa

    def es_triangulo_rectangulo(self) -> bool:
        hipotenusa: float = self.calcular_hipotenusa()
        return (self.base**2 + self.altura**2) == hipotenusa**2


class Rombo:
    def __init__(self, diagonal_mayor: float, diagonal_menor: float) -> None:
        self.diagonal_mayor: float = diagonal_mayor
        self.diagonal_menor: float = diagonal_menor

    def area(self) -> float:
        return (self.diagonal_mayor * self.diagonal_menor) / 2

    def perimetro(self) -> float:
        lado: float = math.sqrt(
            (self.diagonal_mayor / 2) ** 2 + (self.diagonal_menor / 2) ** 2
        )
        return 4 * lado


class Trapecio:
    def __init__(
        self, base_mayor: float, base_menor: float, altura: float
    ) -> None:
        self.base_mayor: float = base_mayor
        self.base_menor: float = base_menor
        self.altura: float = altura

    def area(self) -> float:
        return ((self.base_mayor + self.base_menor) * self.altura) / 2

    def perimetro(self) -> float:
        lado: float = math.sqrt(
            ((self.base_mayor - self.base_menor) / 2) ** 2 + self.altura**2
        )
        return self.base_mayor + self.base_menor + 2 * lado


class PruebaFiguras:
    def __init__(self) -> None:
        self.figuras: list = []

    def agregar_figura(self, figura: object) -> None:
        self.figuras.append(figura)

    def mostrar_atributos(self) -> None:
        for figura in self.figuras:
            print(f"Figura: {type(figura).__name__}")
            for attr, value in figura.__dict__.items():
                print(f"  {attr}: {value}")
            print(f"Área: {figura.area():.2f}")
            print(f"Perímetro: {figura.perimetro():.2f}")
            if isinstance(figura, TrianguloRectangulo):
                print(
                    f"¿Es triángulo rectángulo?: {'Sí' if figura.es_triangulo_rectangulo() else 'No'}"
                )
            print()
            
    def ejecutar_prueba(self) -> None:
        circulo: Circulo = Circulo(5)
        rectangulo: Rectangulo = Rectangulo(4, 6)
        cuadrado: Cuadrado = Cuadrado(3)
        triangulo: TrianguloRectangulo = TrianguloRectangulo(3, 4)
        rombo: Rombo = Rombo(6, 8)
        trapecio: Trapecio = Trapecio(10, 6, 4)

        self.agregar_figura(circulo)
        self.agregar_figura(rectangulo)
        self.agregar_figura(cuadrado)
        self.agregar_figura(triangulo)
        self.agregar_figura(rombo)
        self.agregar_figura(trapecio)
        self.mostrar_atributos()

def main() -> None:
    prueba: PruebaFiguras = PruebaFiguras()
    prueba.ejecutar_prueba()


if __name__ == "__main__":
    main()