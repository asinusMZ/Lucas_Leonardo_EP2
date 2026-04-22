import random


def rolar_dados(quantidade_dados):
    lista_dados = []
    for dado in range(quantidade_dados):
        valor_dado = random.randint(1,6)
        lista_dados.append(valor_dado)
    return lista_dados

def guardar_dado(rolados, guardados, indice):
    guardados.append(rolados[indice])
    rolados.pop(indice)

    return [rolados, guardados]

def remover_dado(rolados, guardados, indice):
    rolados.append(guardados[indice])
    guardados.pop(indice)

    return [rolados, guardados]

def calcula_pontos_regra_simples(rolados):

    cat1 = 0
    cat2 = 0
    cat3 = 0
    cat4 = 0
    cat5 = 0
    cat6 = 0

    for dado in rolados:
        if dado == 1:
            cat1 += 1
        elif dado == 2:
            cat2 += 2
        elif dado == 3:
            cat3 += 3
        elif dado == 4:
            cat4 += 4
        elif dado == 5:
            cat5 += 5
        elif dado == 6:
            cat6 += 6
    
    calculo = {}

    calculo[1] = cat1
    calculo[2] = cat2
    calculo[3] = cat3
    calculo[4] = cat4
    calculo[5] = cat5
    calculo[6] = cat6

    return calculo

def calcula_pontos_soma(dados):
    soma = 0

    for dado in dados:
        soma += dado
        
    return soma

def calcula_pontos_sequencia_baixa(dados):
    contador = 1
    min = 7

    for dado in dados:
        if dado < min:
            min = dado

    atual = min
    i = 0

    while i < len(dados):
        achou = False
        for dado in dados:
            if dado == (atual + 1):
                contador += 1
                atual = dado
                achou = True
                break
        if not achou:
            break
        i += 1
        
    if contador >= 4:
        return 15
    else:
        return 0

def calcula_pontos_sequencia_alta(dados):
    contador = 1
    min = 7

    for dado in dados:
        if dado < min:
            min = dado

    atual = min
    i = 0

    while i < len(dados):
        achou = False
        for dado in dados:
            if dado == (atual + 1):
                contador += 1
                atual = dado
                achou = True
                break
        if not achou:
            break
        i += 1
        
    if contador >= 5:
        return 30
    else:
        return 0

def calcula_pontos_full_house(dados):
    contagem = {}

    for dado in dados:
        if dado not in contagem:
            contagem[dado] = 1
        else:
            contagem[dado] += 1
    
    soma = 0
    if 3 in contagem.values() and 2 in contagem.values():
        for dado in dados:
            soma += dado
        return soma
    else:
        return 0

def calcula_pontos_quadra(dados):
    contagem = {}

    for dado in dados:
        if dado not in contagem:
            contagem[dado] = 1
        else:
            contagem[dado] += 1

    soma = 0
    for quantidade in contagem.values():
        if quantidade >= 4:
            for dado in dados:
                soma += dado
            return soma
    return 0

def calcula_pontos_quina(face_dados):
    contagem = {}

    for dado in face_dados:
        if dado not in contagem:
            contagem[dado] = 1
        else:
            contagem[dado] += 1

    for quantidade in contagem.values():
        if quantidade == 5:
            return 50
    return 0
    
