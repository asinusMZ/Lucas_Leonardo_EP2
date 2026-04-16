import random


def rolar_dados(quantidade_dados):
    lista_dados = []
    for dado in range(quantidade_dados):
        valor_dado = random.randint(1,6)
        lista_dados.append(valor_dado)
    return lista_dados

def guardar_dado(lista_dados, dado_escolhido):
    dados_armazenados = []
    lista_dados_restantes = []
    for dado in lista_dados:
        if dado == dado_escolhido:
            dados_armazenados.append(dado)
        elif dado != dado_escolhido:
            lista_dados_restantes.append(dado)
    return dados_armazenados, lista_dados_restantes
    
