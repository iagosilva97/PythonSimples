import math

# 1 - Acessando o numero pi
print("Valor de pi:", math.pi)
print(f'Valor de pi arredondado: {math.pi:.2f}')
# 2 - Acessando o numero e
print("Valor de e:", math.e)
print(f'Valor de e arredondado: {math.e:.2f}')
# 3 - Arredondamento para cima
num = 10.4
print(math.ceil(num))  # Saída: 11
print(math.floor(num))

#4 - fatorial de um número
num2 = int(input("Digite um número:\n"))
print(math.factorial(num2))

# 5 - potencia de numeros
num3 = int(input("Digite um número:\n"))
print(math.power(num3,5))

# 6 - raiz quadrada
num4 = int(input("Digite um número:\n"))
print(math.sqrt(num4))

# 7 - MDC
mdc = math.gcd(20,70)
print(mdc)

# 8 - Logaritimo
print(math.log(10))


