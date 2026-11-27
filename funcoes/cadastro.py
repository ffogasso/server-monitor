def cadastrar(servidores, utilizacao, tipos, ler_porcentagem):
    print("\n----- Cadastro do Servidor -----")
    nome = input("Nome do servidor: ").strip().upper()

    if nome == "":
        print("Nome inválido!")
        return

    # Impedir servidores duplicados
    if nome in servidores:
        print("Servidor já cadastrado!")
        return

    tipo = input("Finalidade do Servidor: ").strip()

    if tipo == "":
        print("Finalidade inválida!")
        return

    # Informar dados de utilização
    cpu = ler_porcentagem("CPU")
    ram = ler_porcentagem("RAM")
    disco = ler_porcentagem("Disco")

    servidores.append(nome)

    utilizacao.append([cpu, ram, disco])

    tipos[nome] = tipo

    print("Servidor cadastrado com sucesso!")