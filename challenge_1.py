def run():
    user = input('Bienvenido por favor introduzca su nombre: ')
    count_character = len(user)
    print(f'Bienvenido al sistema de pruebas su nombre es: {user}\n y la cantidad de caracteres de su nombre son los siguientes:{count_character}')

if __name__ == '__main__':
    run()