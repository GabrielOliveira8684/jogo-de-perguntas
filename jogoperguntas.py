import random
import os
import platform

def perguntas(qual, contador):
    if qual == 0:
        return (f'\nPERGUNTA NÚMERO {contador}: \nQual tipo de dado usamos para representar números inteiros em Python?')
    elif qual == 1:
        return (f'\nPERGUNTA NÚMERO {contador}: \nQual operador usamos para multiplicação em Python?')
    elif qual == 2:
        return (f'\nPERGUNTA NÚMERO {contador}: \nQual função usamos para imprimir algo na tela em Python?')
    elif qual == 3:
        return (f'\nPERGUNTA NÚMERO {contador}: \nQual operador verifica a igualdade entre dois valores em Python?')
    else:
        return (f'\nPERGUNTA NÚMERO {contador}: \nQual palavra reservada usamos para criar uma função em Python?')

def resposta():
    return input('Digite sua resposta: ')

def incorreta():
    print("RESPOSTA INCORRETA!\n")

def correta(pontos):
    print("\nRESPOSTA CORRETA!!\n")
    return pontos + 1

def invalida():
    print("\nRESPOSTA INVÁLIDA")

def limpa_tela():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

matriz = [
    ["INT", "FLOAT", "STR", "BOOL"],
    ["*", "**", "x", "."],
    ["PRINT", "INPUT", "VAR", "SHOW"],
    ["==", "=", "!=", ">"],
    ["DEF", "FUNC", "FUNCTION", "CREATE"],
]

random.shuffle(matriz)

for contador in range(5):
    random.shuffle(matriz[contador])

pontos = 0
escolha = 0

print("\nBEM-VINDO AO JOGO DE PERGUNTAS PYTHON!\nSEU OBJETIVO É ACERTAR O MÁXIMO DE PERGUNTAS POSSÍVEIS")

contador = 1

if 'INT' in matriz[0]:
    escolha = 0
    pergunta = perguntas(escolha, contador)
    print(pergunta)
    print(f"------------------------------------------------------------------\n| {matriz[0][0]}\n| {matriz[0][1]}\n| {matriz[0][2]}\n| {matriz[0][3]}\n------------------------------------------------------------------")
    resp = resposta()
    if resp.lower() == 'int':
        pontos = correta(pontos)
        limpa_tela()
    else:
        incorreta()
        limpa_tela()
elif '*' in matriz[0]:
    escolha = 1
    pergunta = perguntas(escolha, contador)
    print(pergunta)
    print(f"------------------------------------------------------------------\n| {matriz[0][0]}\n| {matriz[0][1]}\n| {matriz[0][2]}\n| {matriz[0][3]}\n------------------------------------------------------------------")
    resp = resposta()
    if resp.lower() == '*':
        pontos = correta(pontos)
        limpa_tela()
    else:
        incorreta()
        limpa_tela()
elif 'PRINT' in matriz[0]:
    escolha = 2
    pergunta = perguntas(escolha, contador)
    print(pergunta)
    print(f"------------------------------------------------------------------\n| {matriz[0][0]}\n| {matriz[0][1]}\n| {matriz[0][2]}\n| {matriz[0][3]}\n------------------------------------------------------------------")
    resp = resposta()
    if resp.lower() == 'print':
        pontos = correta(pontos)
        limpa_tela()
    else:
        incorreta()
        limpa_tela()
elif '==' in matriz[0]:
    escolha = 3
    pergunta = perguntas(escolha, contador)
    print(pergunta)
    print(f"------------------------------------------------------------------\n| {matriz[0][0]}\n| {matriz[0][1]}\n| {matriz[0][2]}\n| {matriz[0][3]}\n------------------------------------------------------------------")
    resp = resposta()
    if resp.lower() == '==':
        pontos = correta(pontos)
        limpa_tela()
    else:
        incorreta()
        limpa_tela()
elif 'DEF' in matriz[0]:
    escolha = 4
    pergunta = perguntas(escolha, contador)
    print(pergunta)
    print(f"------------------------------------------------------------------\n| {matriz[0][0]}\n| {matriz[0][1]}\n| {matriz[0][2]}\n| {matriz[0][3]}\n------------------------------------------------------------------")
    resp = resposta()
    if resp.lower() == 'def':
        pontos = correta(pontos)
        limpa_tela()
    else:
        incorreta()
        limpa_tela()

contador = 2

if 'INT' in matriz[1]:
    escolha = 0
    pergunta = perguntas(escolha, contador)
    print(pergunta)
    print(f"------------------------------------------------------------------\n| {matriz[1][0]}\n| {matriz[1][1]}\n| {matriz[1][2]}\n| {matriz[1][3]}\n------------------------------------------------------------------")
    resp = resposta()
    if resp.lower() == 'int':
        pontos = correta(pontos)
        limpa_tela()
    else:
        incorreta()
        limpa_tela()
elif '*' in matriz[1]:
    escolha = 1
    pergunta = perguntas(escolha, contador)
    print(pergunta)
    print(f"------------------------------------------------------------------\n| {matriz[1][0]}\n| {matriz[1][1]}\n| {matriz[1][2]}\n| {matriz[1][3]}\n------------------------------------------------------------------")
    resp = resposta()
    if resp.lower() == '*':
        pontos = correta(pontos)
        limpa_tela()
    else:
        incorreta()
        limpa_tela()
elif 'PRINT' in matriz[1]:
    escolha = 2
    pergunta = perguntas(escolha, contador)
    print(pergunta)
    print(f"------------------------------------------------------------------\n| {matriz[1][0]}\n| {matriz[1][1]}\n| {matriz[1][2]}\n| {matriz[1][3]}\n------------------------------------------------------------------")
    resp = resposta()
    if resp.lower() == 'print':
        pontos = correta(pontos)
        limpa_tela()
    else:
        incorreta()
        limpa_tela()
elif '==' in matriz[1]:
    escolha = 3
    pergunta = perguntas(escolha, contador)
    print(pergunta)
    print(f"------------------------------------------------------------------\n| {matriz[1][0]}\n| {matriz[1][1]}\n| {matriz[1][2]}\n| {matriz[1][3]}\n------------------------------------------------------------------")
    resp = resposta()
    if resp.lower() == '==':
        pontos = correta(pontos)
        limpa_tela()
    else:
        incorreta()
        limpa_tela()
elif 'DEF' in matriz[1]:
    escolha = 4
    pergunta = perguntas(escolha, contador)
    print(pergunta)
    print(f"------------------------------------------------------------------\n| {matriz[1][0]}\n| {matriz[1][1]}\n| {matriz[1][2]}\n| {matriz[1][3]}\n------------------------------------------------------------------")
    resp = resposta()
    if resp.lower() == 'def':
        pontos = correta(pontos)
        limpa_tela()
    else:
        incorreta()
        limpa_tela()

contador = 3

if 'INT' in matriz[2]:
    escolha = 0
    pergunta = perguntas(escolha, contador)
    print(pergunta)
    print(f"------------------------------------------------------------------\n| {matriz[2][0]}\n| {matriz[2][1]}\n| {matriz[2][2]}\n| {matriz[2][3]}\n------------------------------------------------------------------")
    resp = resposta()
    if resp.lower() == 'int':
        pontos = correta(pontos)
        limpa_tela()
    else:
        incorreta()
        limpa_tela()
elif '*' in matriz[2]:
    escolha = 1
    pergunta = perguntas(escolha, contador)
    print(pergunta)
    print(f"------------------------------------------------------------------\n| {matriz[2][0]}\n| {matriz[2][1]}\n| {matriz[2][2]}\n| {matriz[2][3]}\n------------------------------------------------------------------")
    resp = resposta()
    if resp.lower() == '*':
        pontos = correta(pontos)
        limpa_tela()
    else:
        incorreta()
        limpa_tela()
elif 'PRINT' in matriz[2]:
    escolha = 2
    pergunta = perguntas(escolha, contador)
    print(pergunta)
    print(f"------------------------------------------------------------------\n| {matriz[2][0]}\n| {matriz[2][1]}\n| {matriz[2][2]}\n| {matriz[2][3]}\n------------------------------------------------------------------")
    resp = resposta()
    if resp.lower() == 'print':
        pontos = correta(pontos)
        limpa_tela()
    else:
        incorreta()
        limpa_tela()
elif '==' in matriz[2]:
    escolha = 3
    pergunta = perguntas(escolha, contador)
    print(pergunta)
    print(f"------------------------------------------------------------------\n| {matriz[2][0]}\n| {matriz[2][1]}\n| {matriz[2][2]}\n| {matriz[2][3]}\n------------------------------------------------------------------")
    resp = resposta()
    if resp.lower() == '==':
        pontos = correta(pontos)
        limpa_tela()
    else:
        incorreta()
        limpa_tela()
elif 'DEF' in matriz[2]:
    escolha = 4
    pergunta = perguntas(escolha, contador)
    print(pergunta)
    print(f"------------------------------------------------------------------\n| {matriz[2][0]}\n| {matriz[2][1]}\n| {matriz[2][2]}\n| {matriz[2][3]}\n------------------------------------------------------------------")
    resp = resposta()
    if resp.lower() == 'def':
        pontos = correta(pontos)
        limpa_tela()
    else:
        incorreta()
        limpa_tela()

contador = 4

if 'INT' in matriz[3]:
    escolha = 0
    pergunta = perguntas(escolha, contador)
    print(pergunta)
    print(f"------------------------------------------------------------------\n| {matriz[3][0]}\n| {matriz[3][1]}\n| {matriz[3][2]}\n| {matriz[3][3]}\n------------------------------------------------------------------")
    resp = resposta()
    if resp.lower() == 'int':
        pontos = correta(pontos)
        limpa_tela()
    else:
        incorreta()
        limpa_tela()
elif '*' in matriz[3]:
    escolha = 1
    pergunta = perguntas(escolha, contador)
    print(pergunta)
    print(f"------------------------------------------------------------------\n| {matriz[3][0]}\n| {matriz[3][1]}\n| {matriz[3][2]}\n| {matriz[3][3]}\n------------------------------------------------------------------")
    resp = resposta()
    if resp.lower() == '*':
        pontos = correta(pontos)
        limpa_tela()
    else:
        incorreta()
        limpa_tela()
elif 'PRINT' in matriz[3]:
    escolha = 2
    pergunta = perguntas(escolha, contador)
    print(pergunta)
    print(f"------------------------------------------------------------------\n| {matriz[3][0]}\n| {matriz[3][1]}\n| {matriz[3][2]}\n| {matriz[3][3]}\n------------------------------------------------------------------")
    resp = resposta()
    if resp.lower() == 'print':
        pontos = correta(pontos)
        limpa_tela()
    else:
        incorreta()
        limpa_tela()
elif '==' in matriz[3]:
    escolha = 3
    pergunta = perguntas(escolha, contador)
    print(pergunta)
    print(f"------------------------------------------------------------------\n| {matriz[3][0]}\n| {matriz[3][1]}\n| {matriz[3][2]}\n| {matriz[3][3]}\n------------------------------------------------------------------")
    resp = resposta()
    if resp.lower() == '==':
        pontos = correta(pontos)
        limpa_tela()
    else:
        incorreta()
        limpa_tela()
elif 'DEF' in matriz[3]:
    escolha = 4
    pergunta = perguntas(escolha, contador)
    print(pergunta)
    print(f"------------------------------------------------------------------\n| {matriz[3][0]}\n| {matriz[3][1]}\n| {matriz[3][2]}\n| {matriz[3][3]}\n------------------------------------------------------------------")
    resp = resposta()
    if resp.lower() == 'def':
        pontos = correta(pontos)
        limpa_tela()
    else:
        incorreta()
        limpa_tela()

contador = 5

if 'INT' in matriz[4]:
    escolha = 0
    pergunta = perguntas(escolha, contador)
    print(pergunta)
    print(f"------------------------------------------------------------------\n| {matriz[4][0]}\n| {matriz[4][1]}\n| {matriz[4][2]}\n| {matriz[4][3]}\n------------------------------------------------------------------")
    resp = resposta()
    if resp.lower() == 'int':
        pontos = correta(pontos)
        limpa_tela()
    else:
        incorreta()
        limpa_tela()
elif '*' in matriz[4]:
    escolha = 1
    pergunta = perguntas(escolha, contador)
    print(pergunta)
    print(f"------------------------------------------------------------------\n| {matriz[4][0]}\n| {matriz[4][1]}\n| {matriz[4][2]}\n| {matriz[4][3]}\n------------------------------------------------------------------")
    resp = resposta()
    if resp.lower() == '*':
        pontos = correta(pontos)
        limpa_tela()
    else:
        incorreta()
        limpa_tela()
elif 'PRINT' in matriz[4]:
    escolha = 2
    pergunta = perguntas(escolha, contador)
    print(pergunta)
    print(f"------------------------------------------------------------------\n| {matriz[4][0]}\n| {matriz[4][1]}\n| {matriz[4][2]}\n| {matriz[4][3]}\n------------------------------------------------------------------")
    resp = resposta()
    if resp.lower() == 'print':
        pontos = correta(pontos)
        limpa_tela()
    else:
        incorreta()
        limpa_tela()
elif '==' in matriz[4]:
    escolha = 3
    pergunta = perguntas(escolha, contador)
    print(pergunta)
    print(f"------------------------------------------------------------------\n| {matriz[4][0]}\n| {matriz[4][1]}\n| {matriz[4][2]}\n| {matriz[4][3]}\n------------------------------------------------------------------")
    resp = resposta()
    if resp.lower() == '==':
        pontos = correta(pontos)
        limpa_tela()
    else:
        incorreta()
        limpa_tela()
elif 'DEF' in matriz[4]:
    escolha = 4
    pergunta = perguntas(escolha, contador)
    print(pergunta)
    print(f"------------------------------------------------------------------\n| {matriz[4][0]}\n| {matriz[4][1]}\n| {matriz[4][2]}\n| {matriz[4][3]}\n------------------------------------------------------------------")
    resp = resposta()
    if resp.lower() == 'def':
        pontos = correta(pontos)
        limpa_tela()
    else:
        incorreta()
        limpa_tela()

print(f'Você fez {pontos} pontos, PARABÉNS!')