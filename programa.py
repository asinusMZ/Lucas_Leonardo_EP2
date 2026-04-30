from funcoes import *
dados_guardados = []

cartela = {    
    'regra_simples':  {
        1:-1,
        2:-1,
        3:-1,
        4:-1,
        5:-1,
        6:-1
    },
    'regra_avancada' : {
        'sem_combinacao':-1,
        'quadra': -1,
        'full_house': -1,
        'sequencia_baixa': -1,
        'sequencia_alta': -1,
        'cinco_iguais': -1
    }
}


for rodada in range(1,13):
    dados = rolar_dados(5)
    rolagem = 0
    opcao = 1


    while opcao != 0:
        print(f"Dados Rolados: {dados}")
        print(f"Dados Guardados: {dados_guardados}")

        print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
        opcao = int(input())

        if opcao == 1:
            print("Digite o índice do dado a ser guardado (0 a 4):")
            indice = int(input())
            guardar_dado(dados, dados_guardados, indice)

        elif opcao == 2:
            print("Digite o índice do dado a ser removido (0 a 4):")
            indice = int(input())
            remover_dado(dados, dados_guardados, indice)

        elif opcao == 3:
            if rolagem >= 2:
                print("Você já usou todas as rerrolagens.")
            else:
                dados = rolar_dados(len(dados))
                rolagem += 1

        elif opcao == 4:
            imprime_cartela(cartela)
        