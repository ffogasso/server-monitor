def atualizar(servidores, utilizacao, ler_porcentagem):
    print("\n----- Atualizar Servidor -----")

    nome = input("Nome do servidor: ").strip().upper()

    if nome not in servidores:
        print("Servidor não encontrado!")
        return

    # Busca o índice do servidor
    i = servidores.index(nome)

    print("\nUtilização atual:")
    print("CPU:", utilizacao[i][0], "%")
    print("RAM:", utilizacao[i][1], "%")
    print("Disco:", utilizacao[i][2], "%")

    print("\nInforme os novos valores:")

    utilizacao[i][0] = ler_porcentagem("CPU")
    utilizacao[i][1] = ler_porcentagem("RAM")
    utilizacao[i][2] = ler_porcentagem("Disco")

    print("Servidor atualizado com sucesso!")

