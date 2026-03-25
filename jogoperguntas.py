pontos = 0

print('\nBEM-VINDO AO JOGO DE PERGUNTAS PYTHON!\nSEU OBJETIVO É ACERTAR O MÁXIMO DE PERGUNTAS POSSÍVEIS')

print('\n---------------------------------\nPERGUNTA NÚMERO 1: \nQual tipo de dado usamos para representar números inteiros em Python? \n1- INT\n2- FLOAT\n3- STR\n4- BOOL\n---------------------------------')
resp = (input('DIGITE SUA RESPOSTA: '))
while resp.lower() not in ['int', 'float', 'str', 'bool']:
    print('RESPOSTA INVÁLIDA')
    print('\n---------------------------------\nPERGUNTA NÚMERO 1: \nQual tipo de dado usamos para representar números inteiros em Python? \n1- INT\n2- FLOAT\n3- STR\n4- BOOL\n---------------------------------')
    resp = (input('DIGITE SUA RESPOSTA: ')) 

if resp.lower() == 'int':
    pontos += 1
    print('\nRESPOSTA CORRETA!!')

else:
    print('\nRESPOSTA INCORRETA!')

print('\n---------------------------------\nPERGUNTA NÚMERO 2: \nQual operador usamos para multiplicação em Python? \n1- X\n2- **\n3- *\n4- .\n---------------------------------')
resp = (input('DIGITE SUA RESPOSTA: '))
while resp.lower() not in ['x', '**', '*', '.']:
    print('RESPOSTA INVÁLIDA')
    print('\n---------------------------------\nPERGUNTA NÚMERO 2: \nQual operador usamos para multiplicação em Python? \n1- X\n2- **\n3- *\n4- .\n---------------------------------')
    resp = (input('DIGITE SUA RESPOSTA: '))

if resp == '*':
    pontos += 1
    print('\nRESPOSTA CORRETA!!')

else:
    print('RESPOSTA INCORRETA!')

print('\n---------------------------------\nPERGUNTA NÚMERO 3: \nQual função usamos para imprimir algo na tela em Python? \n1- print()\n2- input()\n3- var()\n4- show()\n---------------------------------')
resp = (input('DIGITE SUA RESPOSTA: '))
while resp.lower() not in ['print()', 'input()', 'var()', 'show()']:
    print('RESPOSTA INVÁLIDA')
    print('\n---------------------------------\nPERGUNTA NÚMERO 3: \nQual função usamos para imprimir algo na tela em Python? \n1- print()\n2- input()\n3- var()\n4- show()\n---------------------------------')
    resp = (input('DIGITE SUA RESPOSTA: '))

if resp.lower() == 'print()':
    pontos += 1
    print('\nRESPOSTA CORRETA!!')

else:
    print('RESPOSTA INCORRETA!')

print('\n---------------------------------\nPERGUNTA NÚMERO 4: \nQual operador verifica a igualdade entre dois valores em Python? \n1- ==\n2- =\n3- !=\n4- >\n---------------------------------')
resp = (input('DIGITE SUA RESPOSTA: '))
while resp.lower() not in ['==', '=', '!=', '>']:
    print('RESPOSTA INVÁLIDA')
    print('\n---------------------------------\nPERGUNTA NÚMERO 4: \nQual operador verifica a igualdade entre dois valores em Python? \n1- ==\n2- =\n3- !=\n4- >\n---------------------------------')
    resp = (input('DIGITE SUA RESPOSTA: '))

if resp == '==':
    pontos += 1
    print('\nRESPOSTA CORRETA!!')
else:
    print('RESPOSTA INCORRETA!')

print('\n---------------------------------\nPERGUNTA NÚMERO 5: \nQual palavra reservada usamos para criar uma função em Python? \n1- func\n2- def\n3- function\n4- create\n---------------------------------')
resp = (input('DIGITE SUA RESPOSTA: '))
while resp.lower() not in ['func', 'def', 'function', 'create']:
    print('RESPOSTA INVÁLIDA')
    print('\n---------------------------------\nPERGUNTA NÚMERO 5: \nQual palavra reservada usamos para criar uma função em Python? \n1- func\n2- def\n3- function\n4- create\n---------------------------------')
    resp = (input('DIGITE SUA RESPOSTA: '))

if resp.lower() == 'def':
    pontos += 1
    print('\nRESPOSTA CORRETA!!')
else:
    print('RESPOSTA INCORRETA!')

print(f'\n---------------------------------\nFIM DE JOGO!!\nVOCÊ ACERTOU {pontos} PERGUNTAS\n---------------------------------')