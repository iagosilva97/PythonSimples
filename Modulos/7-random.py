import random

# 1 - Selecionar um valor aleatório de uma lista
lista = ['maçã', 'banana', 'laranja', 'uva']
print(random.choice(lista))
print(random.choices(lista, k=2))  # Pode repetir
print(random.sample(lista, k=2))  # Não repete
print(random.shuffle(lista))  # Embaralha a lista
print(lista)

# 2 - Gerar um número aleatório
print(random.random())  # Entre 0 e 1
print(random.randint(1, 10))  # Entre 1 e 10 (inclusivo)
print(random.uniform(1, 10))  # Entre 1 e 10 (float)
print(random.randrange(1, 10, 2))  # Entre 1 e 10 (impares)
print(round(random.uniform(1, 10), 2))  # Entre 1 e 10 (float com 2 casas)

# 3 - Gerar um número aleatório com seed
random.seed(10)  # Define a semente
print(random.random())  # Sempre o mesmo número
random.seed(10)  # Define a semente
print(random.random())  # Sempre o mesmo número
random.seed()  # Semente aleatória
print(random.random())  # Sempre um número diferente

# 4 - Gerar um número aleatório criptograficamente seguro
print(random.SystemRandom().random())  # Entre 0 e 1
print(random.SystemRandom().randint(1, 10))  # Entre 1 e 10 (inclusivo)
print(random.SystemRandom().uniform(1, 10))  # Entre 1 e 10 (float)
print(random.SystemRandom().randrange(1, 10, 2))  # Entre 1 e 10 (impares)
print(round(random.SystemRandom().uniform(1, 10), 2))  # Entre 1 e 10 (float com 2 casas)
print(random.SystemRandom().choice(lista))  # Escolhe um item da lista

# 5 - Gerar uma senha aleatória
caracteres = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()'
senha = ''.join(random.choices(caracteres, k=12))
print(senha)

# 6 - Gerar uma senha aleatória criptograficamente segura
caracteres = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()'
senha = ''.join(random.SystemRandom().choices(caracteres, k=12))
print(senha)

# 7 - Simular um dado
print(random.randint(1, 6))  # Entre 1 e 6 (inclusivo)
print(random.choice([1, 2, 3, 4, 5, 6]))  # Entre 1 e 6 (inclusivo)
print(random.SystemRandom().randint(1, 6))  # Entre 1 e 6 (inclusivo)
print(random.SystemRandom().choice([1, 2, 3, 4, 5, 6]))  # Entre 1 e 6 (inclusivo)

# 8 - Simular o lançamento de uma moeda
print(random.choice(['cara', 'coroa']))
print(random.randint(0, 1))  # 0 ou 1
print(random.SystemRandom().choice(['cara', 'coroa']))
print(random.SystemRandom().randint(0, 1))  # 0 ou 1

# 9 - Simular a roleta russa
print(random.randint(1, 6))  # Entre 1 e 6 (inclusivo)
print(random.choices([1, 2, 3, 4, 5,   6], k=6))  # Entre 1 e 6 (inclusivo)
print(random.SystemRandom().randint(1, 6))  # Entre 1 e 6 (inclusivo)
print(random.SystemRandom().choices([1, 2, 3, 4, 5, 6], k=6))  # Entre 1 e 6 (inclusivo)

# 10 - Simular a loteria
print(random.sample(range(1, 61), k=6))  # 6 números entre 1 e 60
print(random.SystemRandom().sample(range(1, 61), k=6))  # 6 números entre 1 e 60
print(random.sample(range(1, 61), k=6))  # 6 números entre 1 e 60
print(random.SystemRandom().sample(range(1, 61), k=6))  # 6 números entre 1 e 60

# 11 - Simular um sorteio
print(random.choice(['Ana', 'Bruno', 'Carlos', 'Diana']))
print(random.SystemRandom().choice(['Ana', 'Bruno', 'Carlos', 'Diana']))
print(random.choices(['Ana', 'Bruno', 'Carlos', 'Diana'], k=2))  # Pode repetir
print(random.SystemRandom().choices(['Ana', 'Bruno', 'Carlos', 'Diana'], k=2))  # Pode repetir
print(random.sample(['Ana', 'Bruno', 'Carlos', 'Diana'], k=2))  # Não repete
print(random.SystemRandom().sample(['Ana', 'Bruno', 'Carlos', 'Diana'], k=2))  # Não repete