def obter_numero_inteiro(mensagem):
    """
    Função para obter um número inteiro do usuário.
    Continua solicitando até que um valor válido seja fornecido.
    """
    while True:
        try:
            return int(input(mensagem))  # Tenta converter a entrada do usuário para um inteiro
        except ValueError:
            print("Por favor, digite um número inteiro válido.")  # Mensagem de erro se a conversão falhar

def tabuada(t, ate, ordem='crescente'):
    """
    Função para calcular e imprimir a tabuada de um número.
    
    Parâmetros:
    t (int): O número para o qual a tabuada será calculada.
    ate (int): O limite até onde a tabuada será calculada.
    ordem (str): 'crescente' para tabuada crescente ou 'decrescente' para tabuada decrescente.
    """
    if ordem == 'crescente':
        # Imprime a tabuada em ordem crescente
        for c in range(0, ate + 1):
            print(f"{c} x {t} = {c * t}")  # Formata e imprime cada linha da tabuada
    elif ordem == 'decrescente':
        # Imprime a tabuada em ordem decrescente
        for c in range(ate, -1, -1):
            print(f"{c} x {t} = {c * t}")  # Formata e imprime cada linha da tabuada

def main():
    print('======== Tabuada =======')

    # Obtém o número para a tabuada
    t = obter_numero_inteiro("Digite o número que deseja multiplicar: ")

    # Obtém o limite da tabuada, garantindo que seja não negativo
    while True:
        ate = obter_numero_inteiro(f"Digite até quanto você quer multiplicar o '{t}': ")
        if ate >= 0:
            break
        else:
            print("Por favor, digite um número não negativo.")

    # Escolha da ordem da tabuada
    while True:
        ordem = input("Deseja a tabuada em ordem crescente ou decrescente? (crescente/decrescente): ").strip().lower()
        if ordem in ['crescente', 'decrescente']:
            break  # Sai do loop se a entrada for válida
        else:
            print("Opção inválida. Por favor, digite 'crescente' ou 'decrescente'.")  # Mensagem de erro para entrada inválida

    # Exibição da tabuada
    tabuada(t, ate, ordem)  # Chama a função para exibir a tabuada
    print("Fim")  # Mensagem indicando que o programa terminou

if __name__ == "__main__":
    main()  # Chama a função principal
