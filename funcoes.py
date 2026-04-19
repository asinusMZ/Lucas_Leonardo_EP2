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