pontos = 0
def incorreta():
    print('RESPOSTA INCORRETA!')

def correta(pontos):
    print('\nRESPOSTA CORRETA!!')
    return pontos + 1

def invalida():
    print('\nRESPOSTA INVÁLIDA')
    print('---------------------------------\nPERGUNTA NÚMERO 1: \nQual tipo de dado usamos para representar números inteiros em Python? \n1- INT\n2- FLOAT\n3- STR\n4- BOOL\n---------------------------------')
print('\nBEM-VINDO AO JOGO DE PERGUNTAS PYTHON!\nSEU OBJETIVO É ACERTAR O MÁXIMO DE PERGUNTAS POSSÍVEIS')

print('---------------------------------\nPERGUNTA NÚMERO 1: \nQual tipo de dado usamos para representar números inteiros em Python? \n1- INT\n2- FLOAT\n3- STR\n4- BOOL\n---------------------------------')
resp = int(input('DIGITE SUA RESPOSTA: '))
while resp not in [1, 2, 3, 4]:
    invalida()
    resp = int(input('DIGITE SUA RESPOSTA: ')) 

if resp == 1:
    pontos = correta(pontos)
else:
    incorreta()

print('---------------------------------\nPERGUNTA NÚMERO 2: \nQual operador usamos para multiplicação em Python? \n1- X\n2- **\n3- *\n4- .\n---------------------------------')
resp = int(input('DIGITE SUA RESPOSTA: '))
while resp not in [1, 2, 3, 4]:
    invalida()
    resp = int(input('DIGITE SUA RESPOSTA: '))

if resp == 3:
    pontos = correta(pontos)
else:
    incorreta()

print('---------------------------------\nPERGUNTA NÚMERO 3: \nQual função usamos para imprimir algo na tela em Python? \n1- print()\n2- input()\n3- var()\n4- show()\n---------------------------------')
resp = int(input('DIGITE SUA RESPOSTA: '))
while resp not in [1, 2, 3, 4]:
    invalida()
    resp = int(input('DIGITE SUA RESPOSTA: '))

if resp == 1:
    pontos = correta(pontos)
else:
    incorreta()

print('---------------------------------\nPERGUNTA NÚMERO 4: \nQual operador verifica a igualdade entre dois valores em Python? \n1- ==\n2- =\n3- !=\n4- >\n---------------------------------')
resp = int(input('DIGITE SUA RESPOSTA: '))
while resp not in [1, 2, 3, 4]:
    invalida()
    resp = int(input('DIGITE SUA RESPOSTA: '))

if resp == 1:
    pontos = correta(pontos)
else:
    incorreta()

print('---------------------------------\nPERGUNTA NÚMERO 5: \nQual palavra reservada usamos para criar uma função em Python? \n1- func\n2- def\n3- function\n4- create\n---------------------------------')
resp = int(input('DIGITE SUA RESPOSTA: '))
while resp not in [1, 2, 3, 4]:
    invalida()
    resp = int(input('DIGITE SUA RESPOSTA: '))

if resp == 2:
    pontos = correta(pontos)
else:
    incorreta()

print(f'---------------------------------\nFIM DE JOGO!!\nVOCÊ ACERTOU {pontos} PERGUNTAS!\n---------------------------------')
