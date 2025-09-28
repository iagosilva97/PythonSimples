movieList = ["The Holy Grail", "The Life of Brian", "The Meaning of Life"]

#1 - Interando valores de uma lista com while
index = 0
while index < len(movieList):
    print(movieList[index])
    index += 1
    
#2 - Quando a condição for atendida, o loop para
index = 0
while index < len(movieList):
    if movieList[index] == "The Life of Brian":
        break
    print(movieList[index])
    index += 1
    
#3 - Quando a condição for atendida, o loop pula para a próxima iteração
index = 0
while index < len(movieList):
    if movieList[index] == "The Life of Brian":
        index += 1
        continue
    print(movieList[index])
    index += 1

#4 - avaliação do filme
movieName = input("Digite o nome do filme:\n ")
movieRange = int(input("Digite a avaliação do filme de 1 a 5:\n "))
total = 0
count = 0
while count < movieRange:
    note = float(input(f"Digite a nota para o filme:\n "))
    total += note
    count += 1

if movieRange > 0:
    average = total / movieRange
    print(f"A média das notas para o filme {movieName} é: {average}")
    
else:
    avarage = 0
    print("Nenhuma nota foi fornecida.")
    
