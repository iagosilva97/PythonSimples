
# 1 - Fatorial de 1 numero
def fatorial(n):
    if n == 1:
        return 1
    return (n * fatorial(n - 1))
number = int(input("Digite um numero para calcular o fatorial: "))
print(f"O fatorial de {number} é {fatorial(number)}")

# 2 - Soma total de um numero
def soma_total(n):
    if n == 1:
        return 1
    return n + soma_total(n - 1)
number = int(input("Digite um numero para calcular a soma total: "))
print(f"A soma total de {number} é {soma_total(number)}")

