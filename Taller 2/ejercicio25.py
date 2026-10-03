from enum import Enum

class TipodeCuenta(Enum):
    AHORROS = "Ahorros"
    CORRIENTE = "Corriente"  


class CuentaBancaria: 
    def __init__(self, nombresTitular: str, apellidosTitular: str, númeroCuenta: int, tipoCuenta: TipodeCuenta, saldo: float = 0.0,interesMensual: float = 0.0 ) -> None:
        self.nombresTitular: str = nombresTitular
        self.apellidosTitular: str = apellidosTitular
        self.númeroCuenta: int = númeroCuenta
        self.tipoCuenta: TipodeCuenta = tipoCuenta
        self.saldo: float = saldo
        self.interesMensual: float = interesMensual  
        
    def calcularInteres(self) -> float:
        return self.saldo * (self.interesMensual / 100.0)

    def aplicarInteresMensual(self) -> float:
        interes_generado = self.calcularInteres()
        self.saldo += interes_generado
        print(f"Interés mensual del {self.interesMensual}% aplicado a la cuenta {self.númeroCuenta}.")
        print(f"Interés generado: ${interes_generado:.2f} | Nuevo saldo: ${self.saldo:.2f}")
        return self.saldo

    def imprimir(self) -> None: 
        print(f"Nombres del titular = {self.nombresTitular}")
        print(f"Apellidos del titular = {self.apellidosTitular}")
        print(f"Número de cuenta = {self.númeroCuenta}")
        print(f"Tipo de cuenta = {self.tipoCuenta.value}")
        print(f"Tasa de interés mensual = {self.interesMensual}%")
        print(f"Saldo = ${self.saldo:.2f}")
        print(f"Interés mensual generado = ${self.calcularInteres():.2f}")

    def consultarSaldo(self) -> None:
        print("Consultando saldo...")
        print(f"El saldo actual de la cuenta {self.númeroCuenta} es = ${self.saldo:.2f}")
        
    def consignar(self, valor: float) -> bool:
        if valor > 0:
            self.saldo += valor
            print(f"Se ha consignado ${valor} en la cuenta {self.númeroCuenta}. Nuevo saldo: ${self.saldo:.2f}")
            return True
        else:
            print("El valor a consignar debe ser mayor que cero.")
            return False
    
    def retirar(self, valor: float) -> bool:
        if 0 < valor <= self.saldo:
            self.saldo -= valor 
            print(f"Se ha retirado ${valor} de la cuenta {self.númeroCuenta}. Nuevo saldo: ${self.saldo:.2f}")
            return True
        else:
            print("El valor a retirar debe ser mayor a cero y menor o igual al saldo actual.")
            return False
        
    def compararCuentas(self, cuenta: "CuentaBancaria") -> None:
        if self.saldo >= cuenta.saldo:
            print(f"La cuenta {self.númeroCuenta} (${self.saldo:.2f}) tiene un saldo mayor o igual a la cuenta {cuenta.númeroCuenta} (${cuenta.saldo:.2f}).")
        else:
            print(f"La cuenta {self.númeroCuenta} (${self.saldo:.2f}) tiene un saldo menor a la cuenta {cuenta.númeroCuenta} (${cuenta.saldo:.2f}).")
            
    def transferir(self, cuenta_destino: "CuentaBancaria", valor: float) -> bool:
        if self.retirar(valor):
            cuenta_destino.consignar(valor)
            print(f"Transferencia de ${valor} realizada con éxito a la cuenta {cuenta_destino.númeroCuenta}.")
            return True
        else:
            print("No se pudo realizar la transferencia.")
            return False


def main() -> None:
    cuenta1 = CuentaBancaria("Juan", "Pérez", 123456, TipodeCuenta.AHORROS, saldo=1000.0, interesMensual=1.0)
    cuenta2 = CuentaBancaria("María", "Gómez", 654321, TipodeCuenta.CORRIENTE, saldo=500.0, interesMensual=0.5)

    print("Datos de la cuenta 1:")
    cuenta1.imprimir()

    print("\nDatos de la cuenta 2:")
    cuenta2.imprimir()

    print("\n--- Operaciones en la cuenta 1 ---")
    cuenta1.consultarSaldo()
    cuenta1.consignar(200.0)
    cuenta1.retirar(150.0)
    
    print("\n--- Comparando saldos ---")
    cuenta1.compararCuentas(cuenta2)

    print("\n--- Transferencia ---")
    cuenta1.transferir(cuenta2, 300.0)
    
    print("\nDatos de la cuenta 1 después de la transferencia:")
    cuenta1.imprimir()

    print("\nDatos de la cuenta 2 después de recibir la transferencia:")
    cuenta2.imprimir()

    print("\n--- Aplicando interés mensual ---")
    cuenta1.aplicarInteresMensual()
    print()
    cuenta2.aplicarInteresMensual()


if __name__ == "__main__":
    main()