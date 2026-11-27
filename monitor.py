from funcoes.cadastro import cadastrar
from funcoes.listagem import listar
from funcoes.atualizacao import atualizar
from funcoes.consulta import consultar
from funcoes.remocao import remover
from funcoes.relatorio import relatorio

servidores = []
utilizacao = []
tipos = {}

def ler_porcentagem(recurso):
    while True:
        entrada = input(f"{recurso} (%): ")

        if entrada.isascii() and entrada.isdigit():
            valor = int(entrada)

            if 0 <= valor <= 100:
                return valor

        print("Digite um número de 0 a 100: ")

def verificar_status(valor):
    if valor >= 90:
        return "Crítico"
    elif valor >= 80:
        return "Atenção"
    else:
        return "Normal"

def exibir_servidores(servidores, utilizacao, tipos, i):
    nome = servidores[i]
    recursos = ["CPU", "RAM", "Disco"]

    print("\nServidor: ", nome)
    print("Finalidade: ", tipos[nome])

    for j in range(3):
        valor = utilizacao[i][j]
        status = verificar_status(valor)

        print(f"{recursos[j]}: {valor}% - {status}")

    maior = max(utilizacao[i])
    print("Situação geral: ", verificar_status(maior))

while True:
    print("\n----- Monitoramento de Servidores -----")
    print("1 - Cadastrar servidor")
    print("2 - Listar servidores")
    print("3 - Atualizar utilização")
    print("4 - Consultar servidor")
    print("5 - Remover servidor")
    print("6 - Relatório geral")
    print("0 - Sair")

    opcao = input("Selecione uma opção: ")

    if opcao == "1":
        cadastrar(servidores, utilizacao, tipos, ler_porcentagem)

    elif opcao == "2":
        listar(servidores, tipos)

    elif opcao == "3":
        atualizar(servidores, utilizacao, ler_porcentagem)

    elif opcao == "4":
        consultar(servidores, utilizacao, tipos, exibir_servidores)

    elif opcao == "5":
        remover(servidores, utilizacao, tipos)

    elif opcao == "6":
        relatorio(servidores, utilizacao, tipos, exibir_servidores, verificar_status)

    elif opcao == "0":
        print("Programa encerrado!")
        break

    else:
        print("Opção inválida!")