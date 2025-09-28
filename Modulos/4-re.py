import re
text = "Udemy plataforma com muitos cursos de tecnologia"
# 1 - Indice inicial e final de palavras
# O r significa que a string é raw, ou seja, não interpreta caracteres especiais
match = re.search(r"tecnologia", text)
print(match.start())
print(match.end())
# 2 - buscando o indice que possui o ponto
site = "www.udemy.com"
match2 = re.search(r"\.", site)
print(match2.start())
print(match2.end())
# 3 - Lista de caracteres
texto2 = "Os números de 0 a 9"
match3 = re.findall(r"[0-9]", texto2)
print(match3)
# 4 - Lista de caracteres 2
texto3 = "Os números de 0 a 9"
match4 = re.findall(r"[0-5]", texto3)
print(match4)
# 5 - Lista de caracteres 3
texto4 = "Os números de 0 a 9"
match5 = re.findall(r"[a-z]", texto4)
print(match5)
# 6 - Lista de caracteres 4
texto5 = "Os números de 0 a 9"
match6 = re.findall(r"[A-Z]", texto5)
print(match6)
# 7 - Verificando a inicial de uma string
rule = r'^A'
phrase = ['A casa está suja', 'O dia está lindo', 'Vamos passear']
for f in phrase:
    if re.match(rule,f):
        print(f'Corresponde: {f}')
    else:
        print(f'Não corresponde: {f}')
# 8 - Verificando a final de uma string
rule_end = r'!$'
phrase2 = "O dia está lindo!"
match_end = re.search(rule_end, phrase2)
if match_end:
    print("Corresponde")
else:
    print("Não corresponde")