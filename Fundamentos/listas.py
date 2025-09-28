filmeMatrix = ["Matriz", 1999, 8.7, True]
print(filmeMatrix)

filmeList = ["Harry Potter", "Sherk", "Toy Story", "Matrix"]

# Acessando elementos da lista
print(filmeList[0])  # Primeiro elemento
print(filmeList[2])  # Terceiro elemento
print(filmeList[-1]) # Último elemento
print(filmeList[-2]) # Penúltimo elemento
print(filmeList[1:3]) # Elementos do índice 1 ao 2
print(filmeList[:2])  # Primeiros dois elementos
print(filmeList[1:])  # Do segundo elemento até o final
print(filmeList[:])   # Todos os elementos
print(filmeList[::2]) # Elementos com passo 2
print(filmeList[::-1])# Lista invertida
print(filmeList[1::2])# Elementos a partir do índice 1 com passo 2
print(filmeList[-3::-1]) # Elementos do penúltimo ao primeiro invertidos
print(filmeList[-1:-4:-1]) # Último ao terceiro invertidos
print(filmeList[-1:1:-1])  # Último ao segundo invertidos
print(filmeList[-1:0:-1])  # Último ao primeiro invertidos
print(filmeList[-1::-1])   # Último ao primeiro invertidos
print(filmeList[-2::-1])   # Penúltimo ao primeiro invertidos
print(filmeList[-3::-1])   # Antepenúltimo ao primeiro invertidos
print(filmeList[-4::-1])   # Todos os elementos invertidos
print(filmeList[::1])      # Todos os elementos (passo 1)
print(filmeList[::3])      # Elementos com passo 3
print(filmeList[1:4:2])    # Do segundo ao quarto com passo 2
print(filmeList[0:3:2])    # Do primeiro ao terceiro com passo 2
print(filmeList[1:5:2])    # Do segundo ao quinto com passo 2
print(filmeList[0:4:2])    # Do primeiro ao quarto com passo 2
print(filmeList[::4])      # Elementos com passo 4
print(filmeList[1::3])     # A partir do segundo com passo 3
print(filmeList[2::3])     # A partir do terceiro com passo 3
print(filmeList[3::3])     # A partir do quarto com passo
print(filmeList[::5])      # Elementos com passo 5
print(filmeList[1:5:3])    # Do segundo ao quinto com passo 3
print(filmeList[0:4:3])    # Do primeiro ao quarto com passo 3
print(filmeList[::6])      # Elementos com passo 6
print(filmeList[::7])      # Elementos com passo 7
print(filmeList[::8])      # Elementos com passo 8
print(filmeList[::9])      # Elementos com passo 9
print(filmeList[::10])     # Elementos com passo 10

#tamanho da lista
print(len(filmeList))
#adicionando elementos na lista
filmeList.append("Star Wars")
print(filmeList)
filmeList.append("Senhor dos Anéis")
print(filmeList)
#removendo elementos da lista
filmeList.remove("Sherk")
print(filmeList)
filmeList.remove("Toy Story")
print(filmeList)
filmeList.remove("Matrix")
print(filmeList)
#inserindo elementos em uma posição específica
filmeList.insert(1, "Avatar")
print(filmeList)
filmeList.insert(3, "Titanic")
print(filmeList)
filmeList.insert(0, "Jurassic Park")
print(filmeList)
#removendo o último elemento da lista
filmeList.pop()
print(filmeList)
filmeList.pop()
print(filmeList)
filmeList.pop()
print(filmeList)
filmeList.pop()
print(filmeList)
filmeList.pop()
print(filmeList)
filmeList.pop()
print(filmeList)

#removendo um elemento pelo índice
del filmeList[0]
print(filmeList)

#removendo todos os elementos da lista
filmeList.clear()
print(filmeList)

#ordenando uma lista na sorte
filmeList.sort()
print(filmeList)
filmeList.sort(reverse=True)
print(filmeList)

#copiando uma lista
filmeList2 = filmeList.copy()
print(filmeList2)
filmeList3 = list(filmeList)
print(filmeList3)

#juntando listas
filmeListA = ["A", "B", "C"] # Lista A
filmeListB = [1, 2, 3] # Lista B
# Várias formas de juntar as listas A e B
filmeListC = filmeListA + filmeListB # Usando o operador +
print(filmeListC)
filmeListA.extend(filmeListB) # Usando o método extend()
print(filmeListA)
filmeListB.extend(filmeListA) # Usando o método extend()
print(filmeListB)
filmeListA += filmeListB # Usando o operador +=
print(filmeListA)
filmeListB += filmeListA # Usando o operador +=
print(filmeListB)