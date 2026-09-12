saldo=50000
retiro=0
saldo_final=0
print("Cajero Automatico")
clave=input("Ingrese su clave:")
while True:
    print("Bienvenido al cajero automatico")
    print("1:Consultar saldo")
    print("2:Ingresar dinero")
    print("3:Retirar dinero")
    print("4:Salir")
    opcion=input("elija una opcion")
    match opcion:
        case"1":
            print("Su saldo actual es de:", saldo)
        case"2":
            saldo_final=(input("Cuanto desea Ingresar?"))
            while not saldo_final.isdigit():
                saldo_final=input("Cuanto desea Ingresar?")
            saldo_final=int(saldo_final)
            saldo+=saldo_final
            print("Su saldo actual es de:",saldo)
        case"3":
            retiro=(input("Cuanto desea retirar?"))
            while not retiro.isdigit():
                retiro=input("Cuanto desea retirar?")
            retiro=int(retiro)
            saldo-=retiro
            print("Su saldo actual es de:",saldo)
        case"4":
            print("Gracias por usar el cajero automatico\n""Recuerde retirar su tarjeta")
            break
