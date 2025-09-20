filmeDict = {
    "inception": {
        "ano": 2010,
        "diretor": "Christopher Nolan",
        "atores": ["Leonardo DiCaprio", "Joseph Gordon-Levitt", "Ellen Page"],
        "genero": "Ficção Científica",
        "duracao": 148,
        "classificacao": 8.8
},
    "matrix": {
        "ano": 1999,
        "diretor": "Lana Wachowski, Lilly Wachowski",
        "atores": ["Keanu Reeves", "Laurence Fishburne", "Carrie-Anne Moss"],
        "genero": "Ficção Científica",
        "duracao": 136,
        "classificacao": 8.7}
}

print(type(filmeDict))
print(filmeDict)

# acessar os valores do dicionario - titulo
print(filmeDict["inception"])
print(filmeDict["matrix"])
# acessar os valores do dicionario - ano
print(filmeDict["inception"]["ano"])
print(filmeDict["matrix"]["ano"])
#adicionar um novo filme - roteristas
filmeDict["inception"]["roteirista"] = "Christopher Nolan"
filmeDict["matrix"]["roteirista"] = "Lana Wachowski, Lilly Wachowski"
print(filmeDict["inception"])
print(filmeDict["matrix"])
# atualizar o valor da classificação
filmeDict["inception"]["classificacao"] = 9.0
filmeDict["matrix"]["classificacao"] = 8.8
# excluir a duração
del filmeDict["inception"]["duracao"]
del filmeDict["matrix"]["duracao"]
print(filmeDict["inception"])
print(filmeDict["matrix"])


#utilizando pprint para formatar a saída
import pprint
pp = pprint.PrettyPrinter(depth=4)
pp.pprint(filmeDict)
pp.pprint(filmeDict["inception"])
pp.pprint(filmeDict["matrix"])