from funcoes import *

cartela = {    
    'regra_simples':  {
        1: -1,
        2: -1,
        3: -1,
        4: -1,
        5: -1,
        6: -1
    },
    'regra_avancada': {
        'sem_combinacao': -1,
        'quadra': -1,
        'full_house': -1,
        'sequencia_baixa': -1,
        'sequencia_alta': -1,
        'cinco_iguais': -1
    }
}

imprime_cartela(cartela)

for rodada in range(1, 13):
    dados_guardados = []
    dados = rolar_dados(5)
    rolagem = 0
    opcao = ""

    while opcao != "0":
        print(f"Dados rolados: {dados}")
        print(f"Dados guardados: {dados_guardados}")

        print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
        opcao = input()

        if opcao == "1":
            print("Digite o índice do dado a ser guardado (0 a 4):")
            entrada = input("")
            if entrada.isdigit() and int(entrada) < len(dados):
                indice = int(entrada)
                guardar_dado(dados, dados_guardados, indice)
            opcao = "-1"

        elif opcao == "2":
            print("Digite o índice do dado a ser removido (0 a 4):")
            entrada = input("")
            if entrada.isdigit() and int(entrada) < len(dados_guardados):
                indice = int(entrada)
                remover_dado(dados, dados_guardados, indice)
            opcao = "-1"

        elif opcao == "3":
            if rolagem >= 2:
                print("Você já usou todas as rerrolagens.")
            else:
                dados = rolar_dados(len(dados))
                rolagem += 1
            opcao = "-1"

        elif opcao == "4":
            imprime_cartela(cartela)
            opcao = "-1"

        elif opcao == "0":
            jogada_feita = False
            while not jogada_feita:
                print("Digite a combinação desejada:")
                combinacao = input("")

                if combinacao in ['1', '2', '3', '4', '5', '6']:
                    if cartela['regra_simples'][int(combinacao)] != -1:
                        print("Essa combinação já foi utilizada.")
                    else:
                        cartela = faz_jogada(dados + dados_guardados, combinacao, cartela)
                        jogada_feita = True

                elif combinacao in cartela["regra_avancada"]:
                    if cartela["regra_avancada"][combinacao] != -1:
                        print("Essa combinação já foi utilizada.")
                    else:
                        cartela = faz_jogada(dados + dados_guardados, combinacao, cartela)
                        jogada_feita = True

                else:
                    print("Combinação inválida. Tente novamente.")

        else:
            print("Opção inválida. Tente novamente.")

soma_simples = 0
for valor in cartela["regra_simples"].values():
    if valor != -1:
        soma_simples += valor

soma_avancada = 0
for valor in cartela["regra_avancada"].values():
    if valor != -1:
        soma_avancada += valor

pontuacao = soma_avancada + soma_simples

if soma_simples >= 63:
    pontuacao += 35

imprime_cartela(cartela)
print(f"Pontuação total: {pontuacao}")