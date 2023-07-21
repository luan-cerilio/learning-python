from datetime import date
birthYear = int(input('Ano de nascimento: '))
age = date.today().year - birthYear
if age < 18:
    print(f'Ainda vai se alistar (idade: {age}). Faltam {18-age} anos.')
elif age == 18:
    print(f'Hora de se alistar (idade: {age})')
else:
    print(f'Passou do tempo de se alistar (idade: {age}). Excedeu {age-18} anos.')
