def fibonacci(n):
    """Calcula la serie de fibonacci de n.

    return n fibonacci
    """
    if n == 0 or n == 1:
        return 1
    
    return fibonacci(n - 1) + fibonacci(n - 2)


def run():
    n = int(input('Escribe un entero: '))

    print(fibonacci(n))


if __name__ == '__main__':
    run()