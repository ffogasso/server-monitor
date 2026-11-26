# Server Monitor

Sistema de monitoramento e diagnóstico de servidores desenvolvido em Python como projeto acadêmico do primeiro semestre de Ciência da Computação.

## Sobre o projeto

O Server Monitor simula o monitoramento de uma infraestrutura de TI, permitindo gerenciar servidores, acompanhar a utilização de recursos, identificar situações críticas e gerar relatórios de desempenho por meio de uma interface de linha de comando (CLI).

## Funcionalidades

- Cadastro e remoção de servidores.
- Listagem de servidores cadastrados.
- Consulta individual de servidores.
- Atualização da utilização de CPU, RAM e armazenamento.
- Classificação da situação dos servidores.
- Geração de relatórios de desempenho.
- Cálculo da média de utilização dos recursos.
- Validação de entradas.
- Prevenção de cadastros duplicados.
- Organização modular do código.

## Classificação dos recursos

| Utilização | Situação |
|---|---|
| 0% a 79% | Normal |
| 80% a 89% | Atenção |
| 90% a 100% | Crítico |

A situação geral de cada servidor é determinada pelo recurso que apresenta a maior porcentagem de utilização.

## Estrutura do projeto

- `main.py` — Menu principal, estruturas de dados e funções reutilizáveis.
- `funcoes/`
  - `cadastro.py` — Cadastro de servidores.
  - `listagem.py` — Listagem de servidores.
  - `atualizacao.py` — Atualização dos recursos.
  - `consulta.py` — Consulta individual.
  - `remocao.py` — Remoção de servidores.
  - `relatorio.py` — Geração de relatórios e estatísticas.

## Conceitos de programação utilizados

- **Funções definidas pelo usuário:** organizam as operações e evitam a repetição de código.
- **Listas:** armazenam os nomes dos servidores cadastrados.
- **Matrizes:** armazenam os valores de utilização de CPU, RAM e armazenamento.
- **Dicionários:** associam cada servidor à sua respectiva finalidade.
- **Estruturas condicionais:** permitem validar informações e classificar a situação dos recursos.
- **Estruturas de repetição:** permitem percorrer as estruturas de dados e controlar a execução do programa.
- **Modularização:** separa as responsabilidades do sistema em diferentes arquivos.
- **Reutilização de código:** permite utilizar funções auxiliares em diferentes operações.

## Tecnologias utilizadas

- Python 3
- Interface de linha de comando (CLI)
- Git e GitHub
- Sem dependências externas

## Como executar

1. Clone ou baixe este repositório.
2. Abra a pasta do projeto no terminal.
3. Execute o comando `python main.py` ou `python3 main.py`.
4. Selecione a operação desejada no menu principal.

## Limitações

Atualmente, o sistema funciona em um ambiente simulado, no qual os dados de utilização dos servidores são informados manualmente pelo usuário.

As informações são armazenadas em memória durante a execução do programa e não são mantidas após seu encerramento.

Os limites de classificação dos recursos foram definidos para fins acadêmicos.

## Melhorias futuras

- Monitoramento de recursos em tempo real.
- Monitoramento remoto de servidores.
- Armazenamento permanente de dados.
- Alertas automáticos de segurança e desempenho.
- Histórico de utilização dos recursos.
- Interface gráfica.
- Integração com servidores Linux.

## Objetivo acadêmico

O projeto tem como objetivo aplicar os fundamentos da programação na resolução de um problema relacionado à infraestrutura de TI, consolidando conhecimentos de lógica de programação, estruturas de dados, modularização e desenvolvimento de software.

Além disso, busca proporcionar uma introdução prática aos conceitos de monitoramento de infraestrutura e administração de servidores.

## Autores

- [@ffogasso](https://github.com/ffogasso)
- [@pedrosch424](https://github.com/pedrosch424)

---

Desenvolvido como parte do curso de Ciência da Computação.