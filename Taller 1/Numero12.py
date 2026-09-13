class Sueldo:
    @staticmethod
    def Preguntar_Horas(horas):
        print(f"Ingrese las horas trabajadas: ")
        return float(input())
    
    @staticmethod
    def Pago_Horas(pago):
        print(f"Ingrese pago por hora en $: ")
        return float(input())
    
    
    @staticmethod
    def Retencion_fuente(retencion):
        print(f"Ingrese el porcentaje % de retención: ")
        return float(input())
    
    @staticmethod
    def Calcular_sueldo_bruto(horas, pago):
        return horas * pago  
    
    @staticmethod
    def Calcular_retencion(sueldo_bruto, retencion):
        return sueldo_bruto * (retencion / 100)
    
    @staticmethod
    def Calcular_sueldo_neto(sueldo_bruto, retencion):
        return sueldo_bruto - retencion
    
    @staticmethod
    def Printar_resultados(sueldo_bruto, retencion_valor, sueldo_neto):
        print(f"El sueldo bruto es: {sueldo_bruto}")
        print(f"La retención en valor es: {retencion_valor}")
        print(f"El sueldo neto es: {sueldo_neto}")

def main():
    horas = Sueldo.Preguntar_Horas(0)
    pago = Sueldo.Pago_Horas(0)
    retencion = Sueldo.Retencion_fuente(0)
    
    sueldo_bruto = Sueldo.Calcular_sueldo_bruto(horas, pago)
    retencion_valor = Sueldo.Calcular_retencion(sueldo_bruto, retencion)
    sueldo_neto = Sueldo.Calcular_sueldo_neto(sueldo_bruto, retencion_valor)
    
    Sueldo.Printar_resultados(sueldo_bruto, retencion_valor, sueldo_neto)
    

if __name__ == "__main__":
    main()