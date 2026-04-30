from funcoes import *
dados_guardados = []
numero_dados = 5
opcao = 1
for rodada in range(1,13):
    while opcao != 0:
        i = 0
        dados = rolar_dados(numero_dados)
        print(f"Dados Rolados: {dados}")
        print(f"Dados Guardados: {dados_guardados}")
        opcao = int(input("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação: "))
        i += 1
        if opcao == 1:
            indice = int(input("Digite o índice do dado a ser guardado (0 a 4): "))
            guardar_dado(dados, dados_guardados, indice)
        elif opcao == 2:
            if dados_guardados != []:
                indice = int(input("Digite o índice do dado a ser removido (0 a 4): "))
                remover_dado(dados, dados_guardados, indice)
        elif opcao == 3:
            if i > 2:
                print("Você já usou todas as rerrolagens.")
        elif opcao == 4:
            cartela = imprime_cartela
        
        
