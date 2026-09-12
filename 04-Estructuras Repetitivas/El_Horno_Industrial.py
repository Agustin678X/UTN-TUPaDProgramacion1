while True:
    temperatura = input("Ingrese la temperatura, para salir ingrese 'FIN': ").strip().upper()
    if temperatura == "FIN":
        print("Saliendo del programa.")
        break
    if temperatura == "":
        print("La temperatura no puede estar vacia.")
        continue
    cont_puntos = 0
    es_digito = True
    for i in temperatura:
            if i == '.':
                cont_puntos += 1
            elif not i.isdigit():
                es_digito = False
                break
    if cont_puntos > 1 or not es_digito: 
                    print('La temperatura debe ser un número entero o decimal positivo.')
                    continue
    temperatura = float(temperatura)
    if temperatura < 100 or temperatura > 500:
        print("¡ADVERTENCIA! Temperatura fuera de rango")
    print("Temperatura registrada")