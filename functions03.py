from time import sleep

def contador(i, f, p):
    p = abs(p)
    if p == 0:
        p = 1
    if i < f:
        print(f'Contagem de {i} até {f} de {p} em {p}')
        for el in range(i, f+1, p):
            print(el, end=' ')
            sleep(0.5)
        print('FIM!')
        print('-'*30)
    elif i > f:
        print(f'Contagem de {i} até {f} de {p} em {p}')
        for el in range(i, f-1, -p):
           print(el, end=' ')
           sleep(0.5)
        print('FIM!')
        print('-'*30)

def contadorCustom():
    print('Faça sua contagem!')
    i = int(input('Início: '))
    f = int(input('Fim: '))
    p = int(input('Passo: '))
    return contador(i, f, p)
    print('-'*30)


contador(1, 10, 1)
contador(10, 0, 2)
contador(20, 10, -1)
contadorCustom()


