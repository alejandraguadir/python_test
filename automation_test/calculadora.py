def suma(x, y):
    return x + y

def resta(x, y):
    return x - y

def multiplica(x, y):
    return x * y

def dividir(x, y):
    if y == 0:
        raise ValueError("No se puede dividir por cero")
    return x / y
