class Operaciones:
    @staticmethod
    def preguntar_Suma(Suma):
        print(f"Ingrese el inicial ")
        return float(input())
    
    @staticmethod
    def Preguntar_X(x):
        print(f"Ingrese el valor de X ")
        return float(input())
    
    @staticmethod
    def Preguntar_Y(Y):
        print(f"Ingrese el valor de Y ")
        return float(input())
    
    @staticmethod
    def calcular_Suma(Suma, x):
        return Suma + x
    
    @staticmethod
    def calcular_nueva_X(X, Y):
        return X + (Y**2)
    
    @staticmethod
    def calcular_nuevasuma(suma, nuevaX, Y):
        return suma + (nuevaX/Y)


def main():
   Suma = Operaciones.preguntar_Suma(0)
   X = Operaciones.Preguntar_X(20)
   
   SegundaSuma= Operaciones.calcular_Suma(Suma, X)
   
   Y = Operaciones.Preguntar_Y(0)
   nuevaX = Operaciones.calcular_nueva_X(X, Y)
   
   NuevaSuma = Operaciones.calcular_nuevasuma(SegundaSuma, nuevaX, Y)
   
   print(f"El resultado de la suma es: {NuevaSuma}")


if __name__ == "__main__":
    main()