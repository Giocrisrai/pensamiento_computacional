def run():
    user_1 = input('Buenas tardes ingresar el nombre del primer usuario: ')
    age_1 = int(input('Ingrese la edad del primer usuario: '))
    user_2 = input('Buenas tardes ingresar el nombre del segundo usuario: ')
    age_2 = int(input('Ingrese la edad del segundo usuario: '))

    if age_1 > age_2:
        print(f'El usuario {user_1} es mayor al usuario {user_2}')
    elif age_2 > age_1:
        print(f'El usuario {user_2} es mayor al usuario {user_1}')
    else:
        print(f'Los usuarios {user_1} y {user_2} tienen la misma edad')

if __name__ == '__main__':
    run()