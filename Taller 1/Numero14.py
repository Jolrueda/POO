class SquareandCube:
    @staticmethod
    def preguntar_Numero():
        print(f"Ingrese el inicial: ")
        return float(input())
    
    def Numero_cuadrado(numero):
        return numero ** 2
    
    def Numero_cubo(numero):
        return numero ** 3
    
    def Printar_resultados(numero, cuadrado, cubo):
        print(f"El número ingresado es: {numero}")
        print(f"El cuadrado del número es: {cuadrado}")
        print(f"El cubo del número es: {cubo}")
    

def main():
   numero = SquareandCube.preguntar_Numero()
   cuadrado = SquareandCube.Numero_cuadrado(numero)
   cubo = SquareandCube.Numero_cubo(numero)
   SquareandCube.Printar_resultados(numero, cuadrado, cubo)


if __name__ == "__main__":
    main()