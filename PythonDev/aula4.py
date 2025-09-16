#Concatenação de valores

#alternativa 1

name = str(input("Digite o nome do filme: \n"))
yearLaunch = int(input("Digite o ano de lançamento: \n"))
note = float(input("Digite a nota do filme: \n"))

print("Dados do filme")
print("============================")
print("Nome do filme: ",name)
print("Ano de lançamento: ",yearLaunch)
print("Nota do filme: ",note)

#alternativa 2

print("Nome do filme: ",name, "\nAno de lançamento: ",yearLaunch, "\nNota do filme: ",note)

#alternativa 3

print(f"Nome do filme: {name}\n"f"Ano de lançamento: {yearLaunch}\n"f"Nota do filme: {note}")