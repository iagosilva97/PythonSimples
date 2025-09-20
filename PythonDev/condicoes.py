#informações do filme
name = input("Digite o nome do filme: ")
year = int(input("Digite o ano de lançamento do filme: "))
rating = float(input("Digite a classificação do filme (0.0 a 10.0): "))
duration = int(input("Digite a duração do filme em minutos: "))
genre = input("Digite o gênero do filme: ")

#condições
if rating >= 7.0:
    print(f'O filme {name} é considerado um ótimo filme.')
elif 5.0 <= rating < 7.0:
    print(f'O filme {name} é considerado um bom filme.')
else:
    print(f'O filme {name} é considerado um filme ruim.')

if duration > 120:
    print(f'O filme {name} é um filme longo.')
elif 60 <= duration <= 120:
    print(f'O filme {name} é um filme de duração média.')
else:
    print(f'O filme {name} é um filme curto.')
    
if genre.lower() == 'ação':
    print(f'O filme {name} é um filme de ação.')
elif genre.lower() == 'comédia':
    print(f'O filme {name} é um filme de comédia.')
elif genre.lower() == 'drama':
    print(f'O filme {name} é um filme de drama.')
elif genre.lower() == 'ficção científica':
    print(f'O filme {name} é um filme de ficção científica.')
else:
    print(f'O filme {name} é de um gênero diferente.')

#verificar se o filme é um clássico (lançado antes de 2000)
if year < 2000:
    print(f'O filme {name} é um clássico.')
else:
    print(f'O filme {name} não é um clássico.')

#verificar se o filme é recomendado para menores de 12 anos
if rating >= 8.0 and genre.lower() != 'terror': #lower() para evitar problemas com maiusculas e minusculas
    print(f'O filme {name} é recomendado para menores de 12 anos.')
else:
    print(f'O filme {name} não é recomendado para menores de 12 anos.')
    
#verificar se o filme é adequado para uma maratona (duração total menor que 6 horas)
if duration < 360:
    print(f'O filme {name} é adequado para uma maratona.')
else:
    print(f'O filme {name} não é adequado para uma maratona.')
    
#verificar se o filme é um sucesso de bilheteria (classificação maior que 8.5 e duração menor que 150 minutos)
if rating > 8.5 and duration < 150:
    print(f'O filme {name} é um sucesso de bilheteria.')
else:
    print(f'O filme {name} não é um sucesso de bilheteria.')
#verificar se o filme é um lançamento recente (lançado nos últimos 2 anos)
current_year = 2024
if year >= current_year - 2:
    print(f'O filme {name} é um lançamento recente.')
else:
    print(f'O filme {name} não é um lançamento recente.')
#verificar se o filme é parte de uma franquia (nome do filme contém números ou "Parte")
if any(char.isdigit() for char in name) or 'parte' in name.lower():
    print(f'O filme {name} é parte de uma franquia.')
else:
    print(f'O filme {name} não é parte de uma franquia.')
#verificar se o filme é indicado ao Oscar (classificação maior que 8.0 e gênero drama ou ficção científica)
if rating > 8.0 and genre.lower() in ['drama', 'ficção científica']:
    print(f'O filme {name} é indicado ao Oscar.')
else:
    print(f'O filme {name} não é indicado ao Oscar.')
#verificar se o filme é adequado para todas as idades (classificação maior que 6.0 e gênero não é terror ou suspense)
if rating > 6.0 and genre.lower() not in ['terror', 'suspense']:
    print(f'O filme {name} é adequado para todas as idades.')
else:
    print(f'O filme {name} não é adequado para todas as idades.')