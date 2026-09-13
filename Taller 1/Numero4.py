class Edades:
    @staticmethod
    def preguntar_edad(nombre):
        print(f"Ingrese la edad de {nombre}")
        return float(input())
    
    @staticmethod
    def calcular_edalber(edjuan):
        return 2 * edjuan / 3

    @staticmethod
    def calcular_edana(edjuan):
        return 4 * edjuan / 3

    @staticmethod
    def calcular_edmama(edjuan, edalber, edana):
        return edjuan + edalber + edana
    
    @staticmethod
    def imprimir_edades(edjuan, edalber, edana, edmama):
        print(f"Edad de Alberto: {edalber}")
        print(f"Edad de Ana: {edana}")
        print(f"Edad de Juan: {edjuan}")
        print(f"Edad de la Mama: {edmama}")


def main():
    edjuan = Edades.preguntar_edad("Juan")
    
    edalber = Edades.calcular_edalber(edjuan)
    edana = Edades.calcular_edana(edjuan)
    edmama = Edades.calcular_edmama(edjuan, edalber, edana)

    Edades.imprimir_edades(edjuan, edalber, edana, edmama)


if __name__ == "__main__":
    main()