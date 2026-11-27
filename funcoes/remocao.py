def remover(servidores, utilizacao, tipos):
    print("\n----- Remover Servidor -----")

    nome = input("Nome do servidor: ").strip().upper()

    if nome not in servidores:
        print("Servidor não encontrado!")
        return

    confirmacao = input("Confirma a remoção? (S/N): ").upper()

    if confirmacao != "S":
        print("Remoção cancelada!")
        return

    i = servidores.index(nome)

    servidores.pop(i)
    utilizacao.pop(i)

    del tipos[nome]

    print("Servidor removido com sucesso!")