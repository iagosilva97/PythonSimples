#utilizando o dicionario
filmesDict = {
    'Star Wars': 1977,
    'Matrix': 1999,
    'Senhor dos Anéis': 2001,
    'Clube da Luta': 1999,
    'Forrest Gump': 1994,
    'Toy Story': 1995,
    'Sherk': 2001}
print(type(filmesDict))
print(filmesDict)

filmMatrix = {
    'titulo': 'Matrix',
    'ano': 1999,
    'diretor': 'Lana Wachowski, Lilly Wachowski',
    'atores': ['Keanu Reeves', 'Laurence Fishburne', 'Carrie-Anne Moss'],
    'genero': 'Ficção Científica',
    'duracao': 136,
    'classificacao': 8.7
}
print(type(filmMatrix))
print(filmMatrix)
# acessar os valores do dicionario - titulo
print(filmMatrix['titulo'])
# acessar os valores do dicionario - ano
print(filmMatrix['ano'])
# acessar os valores do dicionario - diretor
print(filmMatrix['diretor'])
# acessar os valores do dicionario - atores
print(filmMatrix['atores'])
# acessar os valores do dicionario - genero
print(filmMatrix['genero'])
# acessar os valores do dicionario - duracao
print(filmMatrix['duracao'])
# acessar os valores do dicionario - classificacao
print(filmMatrix['classificacao'])
# acessar os valores do dicionario - primeiro, segundo e terceiro ator
print(filmMatrix['atores'][0])
print(filmMatrix['atores'][1])
print(filmMatrix['atores'][2])
# verificar se a classificação é maior ou igual a 7
print(filmMatrix['classificacao'] >= 7)
# verificar se a duração é maior que 120 minutos
print(filmMatrix['duracao'] > 120)
# verificar se o gênero é 'Ficção Científica'
print(filmMatrix['genero'] == 'Ficção Científica')
# imprimir o nome dos atores separados por vírgula
print(filmMatrix['diretor'].split(', '))
print(', '.join(filmMatrix['atores'])) # juntar os atores em uma string separada por vírgula
# buscar pelo metodo get o valor do diretor
print(filmMatrix.get('diretor'))
# buscar pelo metodo get o valor do roteirista, caso não exista, retornar 'Roteirista não informado'
print(filmMatrix.get('roteirista', 'Roteirista não informado'))
# adicionar o roteirista no dicionario
filmMatrix['roteirista'] = 'Lana Wachowski, Lilly Wachowski'
print(filmMatrix)
# atualizar o valor da classificação
filmMatrix['classificacao'] = 8.8
print(filmMatrix)
# remover o valor da duração
del filmMatrix['duracao']
print(filmMatrix)
# imprimir todas as chaves do dicionario
print(filmMatrix.keys())
# imprimir todos os valores do dicionario
print(filmMatrix.values())
# adicionar um novo filme ao dicionario filmesDict por input do usuário
novoFilme = input('Digite o nome de um filme para adicionar ao dicionário: ')
anoFilme = int(input('Digite o ano de lançamento do filme: '))
filmesDict[novoFilme] = anoFilme
print(filmesDict)
filmesTuplas = tuple(filmesLista)
print(type(filmesTuplas))
print(filmesTuplas)
# transformar a lista em tupla
filmesTuplas = tuple(filmesLista)
print(type(filmesTuplas))
print(filmesTuplas)
print(filmesTuplas)
print(filmesTuplas)