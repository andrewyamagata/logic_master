# String e seus métodos
texto = "Hello, World! Bem vindo"

print(texto)
print(texto[0])
print(texto[7:12])
print(texto[:5])
print(len(texto))
print(texto.count("E"))
print(texto.count("e"))
print(texto.count("He"))
print(texto.find("World"))

print("-"*30)

print(texto.upper())
print(texto.lower())
print(texto.capitalize())
print(texto.title())
print(texto.split())
lista_de_palavras = texto.split()
lista_de_palavras_2 = '-'.join(lista_de_palavras)
print(lista_de_palavras_2)

print("-"*30)

texto2 = '      AULA PYCODEBR     '
print(texto2.strip())
print(texto2.rstrip())
print(texto2.lstrip())

