def consultar(servidores, utilizacao, tipos, exibir_servidor):
    print("\n----- Consultar Servidor -----")

    nome = input("Nome do servidor: ").strip().upper()

    if nome in servidores:
        i = servidores.index(nome)

        exibir_servidor(servidores, utilizacao, tipos, i)

    else:
        print("Servidor não encontrado!")