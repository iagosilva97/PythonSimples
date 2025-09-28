#usando tuplas

filmesTuplas = (
    'Star Wars',
    'Matrix',
    'Senhor dos Anéis',
    'Clube da Luta', 
    'Forrest Gump')

print(type(filmesTuplas))

#1 - buscar os dois primeiros filmes
print(filmesTuplas[0:2])
#2 - buscar os dois últimos filmes
print(filmesTuplas[-2:])
#3 - buscar todos os filmes, menos o primeiro e o último
print(filmesTuplas[1:-1])
#4 - buscar o índice do filme 'Matrix'
print(filmesTuplas.index('Matrix'))
#5 - contar quantos filmes tem na tupla
print(len(filmesTuplas))
#6 - verificar se o filme 'Clube da Luta' está na tupla
print('Clube da Luta' in filmesTuplas)
#7 - verificar se o filme 'Avatar' está na tupla
print('Avatar' in filmesTuplas)
#8 - transformar a tupla em lista
filmesLista = list(filmesTuplas)
print(type(filmesLista))
print(filmesLista)
#9 - adicionar o filme 'Avatar' na lista
filmesLista.append('Avatar')
print(filmesLista)
#10 - transformar a lista em tupla
filmesTuplas = tuple(filmesLista)
print(type(filmesTuplas))
print(filmesTuplas)
#11 - imprimir a tupla em formato de string, separando os filmes por vírgula
print(', '.join(filmesTuplas))
#12 - imprimir cada filme da tupla, um embaixo do outro
for filme in filmesTuplas:
    print(filme)
#13 - imprimir a tupla invertida
print(filmesTuplas[::-1])
#14 - imprimir a tupla em ordem alfabética
print(sorted(filmesTuplas))
#15 - imprimir a tupla em ordem alfabética inversa
print(sorted(filmesTuplas, reverse=True))
#16 - criar uma nova tupla com os filmes 'O Poderoso Chefão' e 'Pulp Fiction' e concatenar com a tupla original
novosFilmes = ('O Poderoso Chefão', 'Pulp Fiction')
filmesTuplas = filmesTuplas + novosFilmes
print(filmesTuplas)
#17 - contar quantas vezes o filme 'Matrix' aparece na tupla
print(filmesTuplas.count('Matrix'))
#18 - encontrar o índice do filme 'Forrest Gump' a partir do índice 2
print(filmesTuplas.index('Forrest Gump', 2))
#19 - desempacotar a tupla em variáveis
filme1, filme2, filme3, filme4, filme5, filme6, filme7, filme8 = filmesTuplas
print(filme1)
print(filme2)
print(filme3)
print(filme4)
print(filme5)
print(filme6)
print(filme7)
print(filme8)
#20 - criar uma tupla com os números de 1 a 10 e imprimir apenas os números pares
numeros = (1,2,3,4,5,6,7,8,9,10)
for numero in numeros:
    if numero % 2 == 0:
        print(numero)
#21 - Adiconar um novo filme na tupla apartir de um input do usuário
novoFilme = input('Digite o nome de um filme para adicionar na tupla: ')
filmesLista = list(filmesTuplas)
filmesLista.append(novoFilme)
filmesTuplas = tuple(filmesLista)
print(filmesTuplas)
#22 - Remover um filme da tupla apartir de um input do usuário
filmeRemover = input('Digite o nome de um filme para remover da tupla: ')
filmesLista = list(filmesTuplas)
if filmeRemover in filmesLista:
    filmesLista.remove(filmeRemover)
else:
    print('Filme não encontrado na tupla.')
filmesTuplas = tuple(filmesLista)
print(filmesTuplas)
