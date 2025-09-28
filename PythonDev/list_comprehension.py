# 1 - Lista de 0 a 10 que sejam menores do que 4
listaNumbers = [i for i in range(10) if i < 4]
print(listaNumbers)

movieList = ["The Holy Grail", "The Life of Brian", "The Meaning of Life"]

# 2 - Filmes que possuem a palavra "Life" no nome
moviesWithLife = [movie for movie in movieList if "Life" in movie]
print(moviesWithLife)

# 3 - Filmes com mais de 15 caracteres
longNamedMovies = [movie for movie in movieList if len(movie) > 15]
print(longNamedMovies)

# 4 - Filmes que não assistimos
watchedMovies = ["The Holy Grail", "The Meaning of Life"]
unwatchedMovies = [movie for movie in movieList if movie not in watchedMovies]
print(unwatchedMovies)

# 5 - Encontrando um filme pelo nome
while True:
    searchName = input("Digite o nome do filme que deseja encontrar (ou sair para encerrar):\n ")
    if searchName.lower() == "sair":
        print("Encerrando a busca.")
        break
    foundMovies = [movie for movie in movieList if searchName.lower() in movie.lower()]
    if foundMovies:
        print(f"Filmes encontrados: {foundMovies}")
        for found in foundMovies:
            print(found)
    else:
        print("Nenhum filme encontrado com esse nome.")
    