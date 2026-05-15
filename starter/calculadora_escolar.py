prova_1 = float(input('Digite a nota da prova 1: '))
prova_2 = float(input('Digite a nota da prova 2: '))
prova_3 = float(input('Digite a nota da prova 3: '))

media = (prova_1 + prova_2 + prova_3)/3
media = round(media, 2)

if media < 5:
    print(f'A média foi de {media}, por isso está de reprovado')
elif media < 7:
    print(f'A média foi de {media}, por isso está de recuperação')
else:
    print(f'A média foi de {media}, por isso está aprovado')
