
# Solicita ao usuário que digite um número
t = int(input("Digite o número que deseja multiplicar: "))

# Solicita ao usuário até qual número deseja multiplicar
ate = int(input(f"Digite até quanto você quer multiplicar o '{t}': "))

# Laço que itera de 0 até 'ate' (inclusive)
for c in range(0, ate + 1):
    # Imprime a multiplicação do número 't' pelo contador 'c'
    print("{} x {} = {}".format(c, t, c * t))

# Mensagem de fim
print("Fim")
