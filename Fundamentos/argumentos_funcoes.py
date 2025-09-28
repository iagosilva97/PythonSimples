# 1 - Função para imprimir um nome completo
def full_name(first_name, last_name):
    print(f"Nome completo: {first_name} {last_name}")
    
full_name("Ana", "Silva")
full_name("Carlos", "Santos")
full_name("Maria", "Oliveira")

# 2 - Função para somar dois números
def sum_numbers(num1, num2):
    return num1 + num2
print("Soma:", sum_numbers(5, 10))
print("Soma:", sum_numbers(20, 30))

# 3 - Função com parametro default
def address(conuntry="Brasil"):
    print(f"País: {conuntry}")

address()
address("Portugal")

# 4 - Função para avaliar filme
def rate_movie(num_ratting, movie_name):
    total = 0
    for i in range(num_ratting):
        rating = float(input("Digite a nota para o filme:"))
        total += rating
    if num_ratting > 0:
        average = total / num_ratting
    else:
        average = 0
    print(f"A média das notas para o filme {movie_name} é: {average}")

rate_movie(3, "Inception")
rate_movie(2, "Matrix")

