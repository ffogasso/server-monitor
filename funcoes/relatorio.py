def relatorio(servidores, utilizacao, tipos,
              exibir_servidor, verificar_status):

    print("\n----- Relatório Geral -----")

    quantidade = len(servidores)

    if quantidade == 0:
        print("Nenhum servidor cadastrado!")
        return

    normais = 0
    atencao = 0
    criticos = 0

    somas = [0, 0, 0]

    recursos = ["CPU", "RAM", "Disco"]

    for i in range(quantidade):
        exibir_servidor(servidores, utilizacao, tipos, i)

        maior = max(utilizacao[i])
        status = verificar_status(maior)

        if status == "Critico":
            criticos += 1

        elif status == "Atenção":
            atencao += 1

        else:
            normais += 1

        for j in range(3):
            somas[j] += utilizacao[i][j]

    print("\n----- Resumo da infraestrutura -----")

    print("Total de servidores: ", quantidade)
    print("Servidores normais: ", normais)
    print("Servidores em atençao: ", atencao)
    print("Servidores criticos: ", criticos)

    print("\n----- Media da Utilização -----")

    for j in range(3):
        media = somas[j] / quantidade

        print(f"Media de {recursos[j]}: {media:.2f}%")