def area(a, b):
    aTerreno = a * b
    print(f'A área de um terreno {a}x{b} é de {aTerreno}m².')


print(' ÁREA TERRENO ')
print('-'*14)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)


