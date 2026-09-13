class Circulo:
    @staticmethod
    def preguntar_Radio():
        print(f"Ingrese el radio: ")
        return float(input())
    
    def Area_circulo(numero):
        return 3.14159 * numero ** 2
    
    def Longitud_circunferencia(numero):
        return 2 * 3.14159 * numero
    
    def Printar_resultados(numero, area, longitud):
        print(f"El radio ingresado es: {numero}")
        print(f"El área del círculo es: {area}")
        print(f"La longitud de la circunferencia es: {longitud}")
    

def main():
   numero = Circulo.preguntar_Radio()
   area = Circulo.Area_circulo(numero)
   longitud = Circulo.Longitud_circunferencia(numero)
   Circulo.Printar_resultados(numero, area, longitud)


if __name__ == "__main__":
    main()