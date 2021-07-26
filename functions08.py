def ficha(jog='<não informado>', gol=0):
    print('-'*45)
    print(f'O jogador {jog} fez {gol} gols no campeonato.')


j = str(input('Nome do jogador: '))
g = str(input('Nº de gols marcados: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if j.strip() == '':
    ficha(gol=g)
else:
    ficha(j, g)




    