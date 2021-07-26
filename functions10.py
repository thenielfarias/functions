'''def notas(*notas, status=False):
    fichaAluno = {}
    fichaAluno["notas"] = notas
    fichaAluno["total"] = len(fichaAluno["notas"])
    fichaAluno["maior"] = max(fichaAluno["notas"])
    fichaAluno["menor"] = sorted(fichaAluno["notas"])[0]
    
    soma = 0
    cont = 0    
    for el in fichaAluno["notas"]:
        soma += fichaAluno["notas"][cont]
        cont += 1
    média = soma / len(fichaAluno["notas"])
    fichaAluno["média"] = média
    
    if média < 5:
        conceito = 'RUIM'
    elif média <= 7:
        conceito = 'RAZOÁVEL'
    elif média <= 9:
        conceito = 'BOM'
    else:
        conceito = 'EXCELENTE'
    
    if status:
        fichaAluno["status"] = conceito
        del fichaAluno["notas"]
        return fichaAluno
    else:
        del fichaAluno["notas"]
        return fichaAluno


aluno = notas(8, 5, 7, 8, 10, status=True)
print(aluno)'''


#refatoração
def notas(*notas, status=False):
    fichaAluno = {}
    fichaAluno["total"] = len(notas)
    fichaAluno["maior"] = max(notas)
    fichaAluno["menor"] = min(notas)
    fichaAluno["media"] = sum(notas)/len(notas)    
    if status:
        if fichaAluno["media"] < 5:
            fichaAluno["status"] = 'RUIM'
        elif fichaAluno["media"] <= 7:
            fichaAluno["status"] = 'RAZOÁVEL'
        elif fichaAluno["media"] <= 9:
            fichaAluno["status"] = 'BOM'
        else:
            fichaAluno["status"] = 'EXCELENTE'
    return fichaAluno


aluno = notas(10, 5, 4.5, 6, 9, status=False)
print(aluno)


