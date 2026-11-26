def listar(servidores, tipos):
    print("\n----- Servidores Cadastrados -----")

    if len(servidores) == 0:
        print("Nenhum servidor cadastrado!")
        return
    for i in range(len(servidores)):
        nome = servidores[i]

        print(f"{i + 1} - {nome}")
        print("Finalidade: ", tipos[nome])

    print("Total de servidores: ", len(servidores))