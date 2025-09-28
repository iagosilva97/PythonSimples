# 1 - Função de potencia de um numero
power = lambda num: num ** 2
print(power(5))
print(power(10))
print(power(20))

#Funçaõ que verifica se o numero é par
is_even = lambda num: num % 2 == 0
print(is_even(5))
print(is_even(10))
print(is_even(20))
print(is_even(21))

# Função que divide dois numeros
divide = lambda x, y: x / y
print(divide(10, 2))
print(divide(20, 4))
print(divide(15, 3))

#Função que inverte uma string
reverse_string = lambda s: s[::-1]
print(reverse_string("Python"))
print(reverse_string("Lambda"))
print(reverse_string("Function"))

# Funcionalidades relacionadas aos filmes
movies_list = ["Star Wars", "Matrix", "Senhor dos Anéis", "Clube da Luta", "Pulp Fiction"]
ratings = {
    "Star Wars": [8.7,9.0,10],
    "Matrix": [8.5, 9.0, 9.5],
    "Senhor dos Anéis": [9.0, 9.5, 10],
    "Clube da Luta": [8.8, 9.0, 9.2],
    "Pulp Fiction": [8.9, 9.1, 9.3]
}

# função para calcular a média das avaliações
average_rating = lambda movie_name: sum(ratings[movie_name]) / len(ratings[movie_name])
print(f"A média de avaliações de Star Wars é {average_rating('Star Wars')}")

# função que verifica se o filme está na lista
is_in_list = lambda movie_name: movie_name in movies_list
print(f"Matrix está na lista? {is_in_list('Matrix')}")

# função para recoemndar um filme baseado na média das avaliações
recommend_movie = lambda: max(ratings, key=average_rating)
print(f"Filme recomendado: {recommend_movie()}")
