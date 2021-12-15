def enumeracion_exhaustiva(objetivo):
    respuesta = 0

    while respuesta**2 < objetivo:
        print(respuesta)
        respuesta += 1

    if respuesta**2 == objetivo:
        print(f'La raiz cuadrada de {objetivo} es {respuesta}')
    else:
        print(f'{objetivo} no tiene una raiz cuadarada exacta')

def aproximacion(objetivo):
    epsilon = 0.01
    paso = epsilon**2
    respuesta = 0.0

    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        print(abs(respuesta**2 - objetivo), respuesta)
        respuesta += paso

    if abs(respuesta**2 - objetivo) >= epsilon:
        print(f'No se encontro la raiz cuadrada {objetivo}')
    else:
        print(f'La raiz cuadara de {objetivo} es {respuesta}')

def busqueda_binaria(objetivo):
    epsilon = 0.01
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto +bajo) / 2

    while(abs(respuesta**2 - objetivo)) >= epsilon:
        print(f'bajo={bajo}, alto={alto}, respuesta={respuesta}')
        if respuesta** 2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta
        
        respuesta = (alto + bajo) / 2

    print(f'La raiz cuadrada de {objetivo} es {respuesta}')


def run():
    print(f'Sistema para hallar la raiz cuadrada de un numero entero')
    objetivo = int(input('Escoge un entero: '))
    opcion = int(input('Escriba el metodo con el cual desea calcular la raiz cuadrada del numero. \n 1 enumeracion exhaustiva. \n 2 metodo aproximacion \n 3 busqueda binaria '))

    if opcion == 1:
        enumeracion_exhaustiva(objetivo)
    elif opcion == 2:
        aproximacion(objetivo)
    elif opcion == 3:
        busqueda_binaria(objetivo)
    else:
        print('Escogio una opcion invalida')


if __name__ == '__main__':
    run()