# Programa de Tabuada em Python

Este programa em Python permite que o usuário calcule e exiba a tabuada de um número específico, podendo escolher a ordem de exibição (crescente ou decrescente). O programa é interativo e inclui validação de entrada para garantir que o usuário forneça dados válidos.

## Funcionalidades

- **Entrada do Usuário**: O programa solicita ao usuário que insira um número para o qual a tabuada será calculada e até qual número ele deseja multiplicar.
- **Validação de Dados**: O programa garante que as entradas sejam números inteiros válidos e que o limite da tabuada seja um número não negativo.
- **Escolha da Ordem**: O usuário pode escolher entre visualizar a tabuada em ordem crescente ou decrescente.
- **Exibição da Tabuada**: O programa calcula e exibe a tabuada de acordo com as escolhas do usuário.

## Como Usar

1. Execute o programa em um ambiente Python.
2. Siga as instruções exibidas no terminal para inserir um número e o limite da tabuada.
3. Escolha a ordem de exibição (crescente ou decrescente).
4. A tabuada será exibida no terminal.

## Estrutura do Código

- `obter_numero_inteiro(mensagem)`: Função que solicita um número inteiro ao usuário e valida a entrada.
- `tabuada(t, ate, ordem)`: Função que calcula e imprime a tabuada de um número com base na ordem especificada.
- `main()`: Função principal que orquestra a execução do programa.

## Requisitos

- Python 3.x

## Exemplo de Uso

```bash
$ python tabuada.py
======== Tabuada =======
Digite o número que deseja multiplicar: 5
Digite até quanto você quer multiplicar o '5': 10
Deseja a tabuada em ordem crescente ou decrescente? (crescente/decrescente): crescente
0 x 5 = 0
1 x 5 = 5
2 x 5 = 10
...
10 x 5 = 50
Fim
