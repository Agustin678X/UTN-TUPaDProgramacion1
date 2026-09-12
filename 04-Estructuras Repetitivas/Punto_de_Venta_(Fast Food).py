hamburguesa=4500
papas=2000
bebida=1500
total=0
cambio=0
print("Bienvenido al punto de venta")
while True:
    print("1:Hamburguesa $4500")
    print("2:Papas $2000")
    print("3:Bebida $1500")
    print("4:Pagar")
    print("5:Cancelar pedido")
    opcion=input("elija una opcion")
    match opcion:
        case"1":
            total+=hamburguesa
            print("Hamburguesa agregada. Total actual: $", total)
        case"2":
            total+=papas
            print("Papas agregadas. Total actual: $", total)
        case"3":
            total+=bebida
            print("Bebida agregada. Total actual: $", total)
        case"4":
            print("Su total a pagar es de: $", total)
            pago_total=0
            while True:
                pago=input("Ingrese el monto a pagar:")
                while not pago.isdigit():
                    pago=input("Ingrese el monto a pagar:")
                pago=int(pago)
                pago_total+=pago
                if pago_total>=total:
                    cambio=pago_total-total
                    print("Pago recibido. Su cambio es de: $", cambio)
                    print("Gracias por su compra. Vuelva pronto.")
                    total=0
                    break
                else:
                    print("Monto insuficiente. Le queda por pagar: $",total - pago_total)
        case"5":
            print("Pedido cancelado. Gracias por su visita.")
            total=0
            break
        case _:
            print("Opcion invalida. Por favor, elija una opcion valida.")