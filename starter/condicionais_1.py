print('Olá, Mundo!')

valor = 10

if valor > 5:
    print('O valor é maior que 5.')

print('-'*30)

idade = int(input('Digite sua idade: '))

if idade >= 18:
    print('É maior de idade')
else:
    print('É menor de idade')

print('-'*30)

linguagem = input('Digite uma linguagem: ')

if linguagem == 'Python':
    print('Python é legal')
elif linguagem == 'Java':
    print('Java é difícil')
elif linguagem == 'Cobol':
    print('Cobol é antigo')
else:
    print('Linguagem não identificada')
