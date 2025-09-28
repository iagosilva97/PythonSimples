#estrutura set

filmesSet = {"Star Wars", "Matrix", "Senhor dos Anéis"}
print(type(filmesSet))

#1 - adicionar um filme no set
filmesSet.add("Clube da Luta")
print(filmesSet)
#2 - remover um filme do set
filmesSet.remove("Matrix")
print(filmesSet)
#3 - verificar se um filme está no set
print("Star Wars" in filmesSet)
print("Matrix" in filmesSet)
#4 - contar quantos filmes tem no set
print(len(filmesSet))
#5 - transformar o set em lista
filmesLista = list(filmesSet)
print(type(filmesLista))

# valor true e 1 são considerados iguais
numerosSet = {1, 2, 3, 4, 5, True, False}
print(numerosSet)
print(len(numerosSet))
# remover o valor True
numerosSet.remove(True)
print(numerosSet)
print(len(numerosSet))

#adicionar item de outro set
setA = {1, 2, 3}
setB = {3, 4, 5}
setA.update(setB)
print(setA)
setA = setA.union(setB) # união
print(setA) # união
setA = setA | setB # união
print(setA)