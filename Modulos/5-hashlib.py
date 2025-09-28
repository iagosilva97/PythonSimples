import hashlib

# 1 - Verificando os algoritmos disponíveis
print(hashlib.algorithms_available)

# 2 - Verificando os algoritmos de acordo com o SO
print(hashlib.algorithms_guaranteed)

# 3 - Utilizando o SHA256
algoritmo = hashlib.sha256()
print(algoritimo.digest()) # Retorna o hash em bytes
mensagem = 'Olá, mundo!'.encode()
algoritmo.update(mensagem)
print(algoritmo.hexdigest()) # Retorna o hash em hexadecimal

# 4 - Utilizando o MD5
md5 = hashlib.md5()
md5.update(mensagem)
print(md5.hexdigest())

