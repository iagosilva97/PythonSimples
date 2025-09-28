# 1 - Função para imprimir uma mensagem
def welcome():
    print("Bem-vindo ao programa!")
welcome()
welcome()

for i in range(3):
    welcome()

# 2 - Função para calcular media de notas
def calcular_media():
    num_rating = int(input("Quantas notas você quer inserir? "))
    total = 0
    for _ in range(num_rating):
        nota = float(input("Insira a nota: "))
        total += nota
    if num_rating > 0:
        media = total / num_rating
    else:
        media = 0
    return media

print("A média das notas é:", calcular_media())

# 3 - Função para cadastrar um filme
def create_movie():
    title = input("Título do filme: ")
    director = input("Diretor do filme: ")
    year = input("Ano de lançamento: ")
    movie = {
        "title": title,
        "director": director,
        "year": year
    }
    return movie

print("Filme cadastrado:", create_movie())