def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA'
    elif idade < 18 or idade > 70:
        return f'Com {idade} anos: VOTO FACULTATIVO'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'


print('-'*30)
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))


