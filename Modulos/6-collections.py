from collections import Counter, namedtuple, defaultdict, deque
from operator import itemgetter

# 1 - Lista de frutas (contagem)
frutas = ['banana', 'maçã', 'laranja', 'banana', 'uva', 'maçã', 'banana']
contador = Counter(frutas)
print(contador)
print(contador.most_common(2))  # As 2 frutas mais comuns

# 2 - Tupla nomeada
game = namedtuple("game", ["nome", "preco", "nota"])
g1 = game("The Last of Us", 150, 9.5)
g2 = game("God of War", 120, 9.7)
print(g1)
print(g2.preco)

# 3 - Ordenando Dicionarios
estudantes = {"Pedro":26, "Ana":22, "João":28, "Maria":24}
a = sorted(estudantes.items(), key=itemgetter(0))  # Ordena por nome
b = sorted(estudantes.items(), key=itemgetter(1))  # Ordena por idade
print(a)
print(b)

# 4 - Utilizando uma fila em ambas as estrimidades
deq = deque([20,40,50,60,70])
deq.append(80)  # Adiciona no final
deq.appendleft(10)  # Adiciona no começo
deq.pop()  # Remove do final
deq.popleft()  # Remove do começo
print(deq)