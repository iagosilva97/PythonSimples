movieName = "Top Gun"
movieDescription = """
Top Gun Maverick é um filme de aviação e aventura
muito consagrado na industria
"""

print(movieName.upper())#maiusculo
print(movieName.lower())#minusculo
print(movieName.capitalize())#primeira maiuscula
print(movieName.title())#todas as primeiras maiusculas
print(movieName.strip())#remove espaços desnecessarios
print(movieName.center(10, "-"))#retorna a string centralizada com caracteres adicionais
print(movieName.replace("o", "0"))#substitui caracteres
print(movieName.split(" "))#divide a string em uma lista
print(movieName.find("Gun"))#retorna o indice do inicio da palavra
print(movieName.count("o"))#conta quantas vezes o caractere aparece
