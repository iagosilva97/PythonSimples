movieList = ["The Holy Grail", "The Life of Brian", "The Meaning of Life"]
numeros = [1, 2, 3, 4, 5]

#1 - Interando valores de uma lista

for movie in movieList:
    print(movie)

for numero in numeros:
    print(numero)
    
#2 - utilizando break
for movie in movieList:
    if movie == "The Life of Brian":
        break
    print(movie)
    
#3 - utilizando continue
for movie in movieList:
    if movie == "The Life of Brian":
        continue
    print(movie)
    
#4 - avaliação do filme
movieName = input("Digite o nome do filme:\n ")
movieRange = int(input("Digite a avaliação do filme de 1 a 5:\n "))
total = 0

for i in range(movieRange):
    note = float(input(f"Digite a nota para o filme:\n "))
    total += note

if movieRange > 0:
    average = total / movieRange
    print(f"A média das notas para o filme {movieName} é: {average}")
else:
    avarage = 0
    print("Nenhuma nota foi fornecida.")




