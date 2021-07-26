def leiaInt(userInput):
    ok = False
    valor = 0
    while True:
        n = str(input(userInput))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número válido.\033[m')
        if ok:
            break
    return valor


n = leiaInt('Digite um número: ')
print(f'Número digitado: {n}')


