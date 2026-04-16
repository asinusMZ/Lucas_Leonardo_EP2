import random


def rolar_dados(quantidade_dados):
    lista_dados = []
    for dado in range(quantidade_dados):
        valor_dado = random.randint(1,6)
        lista_dados.append(valor_dado)
    return lista_dados

def guardar_dado(lista_dados, dados_armazenados, dado_escolhido):
    dados_restantes = []
    lista_final_dados = []
    for dado in lista_dados:
        if lista_dados[dado] == dado_escolhido:
            dados_armazenados.append(dado)
        elif lista_dados[dado] != dado_escolhido:
            dados_restantes.append(dado)


    lista_final_dados[0] = dados_restantes
    lista_final_dados[1] = dados_armazenados

    return lista_final_dados
    
