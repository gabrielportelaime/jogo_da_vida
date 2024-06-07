# APENAS UMA SIMULAÇÃO DE COMO A VIDA PODE TER OCORRIDO
import random
import time
import os

jogo_da_vida = []
vivo = "██"
morto = "░░"
separacao = ""
tam_tabuleiro = 100

for i in range(tam_tabuleiro):
    jogo_da_vida.append([])
    for j in range(tam_tabuleiro):
        numero_aleatorio = random.random()
        if(1 - numero_aleatorio < numero_aleatorio):
            criatura = vivo
        else:
            criatura = morto
        jogo_da_vida[i].append(criatura)

os.system('cls')
print('MATRIZ INICIAL:', end="\n\n")
for k in range(tam_tabuleiro):
    print(separacao.join(jogo_da_vida[k]))
time.sleep(1)

matriz_inicial = []
for i in range(tam_tabuleiro):
    matriz_inicial.append([])
    for j in range(tam_tabuleiro):
        matriz_inicial[i].append(jogo_da_vida[i][j])
        
anterior = []
vezes = 0
while(True):
    if(anterior == jogo_da_vida):
        break
    vezes += 1
    anterior = []
    for i in range(tam_tabuleiro):
        anterior.append([])
        for j in range(tam_tabuleiro):
            anterior[i].append(jogo_da_vida[i][j])
    for i in range(1, tam_tabuleiro - 1):
        for j in range(1, tam_tabuleiro - 1):
            vivas = mortas = 0
            for k in range(-1, 2):
                for l in range(-1, 2):
                    if(jogo_da_vida[i + k][j + l] == vivo):
                        vivas += 1
                    else:
                        mortas += 1
            if(jogo_da_vida[i][j] == vivo):
                vivas -= 1
                if(vivas == 0 or vivas > 3):
                    jogo_da_vida[i][j] = morto
            else:
                mortas -= 1
                if(vivas == 3):
                    jogo_da_vida[i][j] = vivo
        os.system('cls')
        for k in range(tam_tabuleiro):
            print(separacao.join(jogo_da_vida[k]))
    # time.sleep(1)

os.system('cls')
print('MATRIZ FINAL:', end="\n\n")
for k in range(tam_tabuleiro):
    print(separacao.join(jogo_da_vida[k]))

print('\nMATRIZ INICIAL:', end="\n\n")
for k in range(tam_tabuleiro):
    print(separacao.join(matriz_inicial[k]))

print('\n\nAcabou na', vezes, 'que processou a matriz inteira')