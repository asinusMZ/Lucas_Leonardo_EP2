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
    i = 0
    while i < len(dados)
        for dado in dados:
            if dado == (min + 1):
                contador += 1
                min = dado

    if contador == 4:
        return 15
    else:
        return 0
