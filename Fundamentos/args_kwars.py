"""
*args and **kwargs in Python
*args usamos quando não sabemos quantos argumentos serão passados para a função.
**kwargs usamos quando não sabemos quantos argumentos nomeados serão passados para a função.
"""

def sum(*num):
    sum_total = 0
    for n in num:
        sum_total += n
    print(f'A soma é {sum_total}')

sum(7)
sum(7, 2)
sum(7, 2, 3)

def cursos(**data):
    for key, value in data.items():
        print(f'{key} - {value}')
print("lista de cursos:")
cursos(nome="Python", duracao="3 meses")
cursos(nome="Java", duracao="4 meses", nivel="Intermediário")
cursos(nome="JavaScript", duracao="6 meses", nivel="Avançado", modulos=10)
cursos(nome="HTML", duracao="1 mês", nivel="Básico", modulos=5, certificado=True)