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
    unicos = sorted(set(dados))
 
    contador = 1
    maior = 1
    for i in range(1, len(unicos)):
        if unicos[i] == unicos[i - 1] + 1:
            contador += 1
            if contador > maior:
                maior = contador
        else:
            contador = 1
 
    if maior >= 4:
        return 15
    else:
        return 0
 
def calcula_pontos_sequencia_alta(dados):
    unicos = sorted(set(dados))
 
    contador = 1
    maior = 1
    for i in range(1, len(unicos)):
        if unicos[i] == unicos[i - 1] + 1:
            contador += 1
            if contador > maior:
                maior = contador
        else:
            contador = 1
 
    if maior >= 5:
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
        if quantidade >= 5:
            return 50
    return 0
    
def calcula_pontos_regra_avancada(dados):
    dicionario_regra = {}
    dicionario_regra["cinco_iguais"] = calcula_pontos_quina(dados)
    dicionario_regra["full_house"] = calcula_pontos_full_house(dados)
    dicionario_regra["quadra"] = calcula_pontos_quadra(dados)
    dicionario_regra["sem_combinacao"] = calcula_pontos_soma(dados)
    dicionario_regra["sequencia_alta"] = calcula_pontos_sequencia_alta(dados)
    dicionario_regra["sequencia_baixa"] = calcula_pontos_sequencia_baixa(dados)
    return dicionario_regra

def faz_jogada(dados, categoria, cartela):
    cartela_atualizada = cartela
    if categoria in ['1','2','3','4','5','6']:
        regra_simples = calcula_pontos_regra_simples(dados)
        for numero, valor in regra_simples.items():
            if numero == int(categoria):
                cartela_atualizada["regra_simples"][numero] = valor
    else:
        regra_avancada = calcula_pontos_regra_avancada(dados)
        for jogada, valor in regra_avancada.items():
            if jogada == categoria:
                cartela_atualizada["regra_avancada"][jogada] = valor
    return cartela_atualizada    

def imprime_cartela(cartela):
    print("Cartela de Pontos:")
    print("-"*25)    
    for i in range(1, 7):
        filler = " " * (15 - len(str(i)))
        if cartela['regra_simples'][i] != -1:
            print(f"| {i}: {filler}| {cartela['regra_simples'][i]:02} |")
        else:
            print(f"| {i}: {filler}|    |")
    for i in cartela['regra_avancada'].keys():
        filler = " " * (15 - len(str(i)))
        if cartela['regra_avancada'][i] != -1:
            print(f"| {i}: {filler}| {cartela['regra_avancada'][i]:02} |")
        else:
            print(f"| {i}: {filler}|    |")
    print("-"*25)
