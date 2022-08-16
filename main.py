#Importação de Bibliotecas
import math

from graphics import *

#Definindo Inicio do Programa
def inicio():
    print(""" 

        Seja Bem Vindo a este programa:

          Trata-se de um programa em Python que, um programa em Python que receba os vértices de um quadrado (p1(x1, y1), p2(x2, y2),p3(x3, y3) e p4(x4, y4)) 
          que deveria estar localizado exatamente no centro de uma janela de 500x500. Levando em conta o sistema de referência do computador. O programa deve receber um valor do
          usuário representando o ângulo da rotação a ser aplicada no quadrado sobre seu ponto central, e devolver os quatro pontos finais, devidamente calculados.
          Ele foi desenvolvido por Pedro Henrique Gomes Sassi aluno do Curso de Ciencia da Computação no IFFAr-FW
          para cumprimento de demanda da matéria de Computação Grafica ministrada pelo professor Dr. Me. Ygor Yepes. 


                            Vamos Começar:

                            """)
    entrada1()

def entrada1():
    global p1x, p1y, p2x, p2y, p3x, p3y, p4x, p4y
    entrada0 = int(input("Digite o tamanho do quadrado de 0 a 500 Pixels: "))
    entrada1 = entrada0 / 2
    p1x = 250 - entrada1
    p1y = 250 - entrada1
    p2x = 250 + entrada1
    p2y = 250 - entrada1
    p3x = 250 - entrada1
    p3y = 250 + entrada1
    p4x = 250 + entrada1
    p4y = 250 + entrada1
    desenho(p1x, p1y, p2x, p2y, p3x, p3y, p4x, p4y)
    return p1x, p1y, p2x, p2y, p3x, p3y, p4x, p4y

def desenho(p1x, p1y, p2x, p2y, p3x, p3y, p4x, p4y):
    win = GraphWin("Coordenadas da tela", 500, 500)
    eixo1 = Line(Point(p1x, p1y), Point(p2x, p2y))
    eixo2 = Line(Point(p2x, p2y), Point(p4x, p4y))
    eixo3 = Line(Point(p4x, p4y), Point(p3x, p3y))
    eixo4 = Line(Point(p3x, p3y), Point(p1x, p1y))
    # desenha os objetos na cena
    eixo1.draw(win)
    eixo2.draw(win)
    eixo3.draw(win)
    eixo4.draw(win)
    win.getMouse() # aguarda click na tela para fechar
    win.close() # encerra a execução
    laco()

def laco():
    repete = int(input("""Escolha uma Opçao
    2 - Girar o cubo;
    5 - Refazer o Cubo;
    8 - Encerrar o Programa.
    Opçâo escolhida: """))

    if repete == 2:
            girar1(p1x, p1y, p2x, p2y, p3x, p3y, p4x, p4y)
    elif repete == 5:
            entrada1()
    elif repete == 8:
        print(""" 

                                      Muito Obrigado por utilizar este programa!

               Att.
               Pedro Henrique Sassi""")
        exit(0)
    else:
            print("Caractere invalido!")
            laco()

def girar1 (p1x, p1y, p2x, p2y, p3x, p3y, p4x, p4y):
    angulo1 = int(input("Digite quantos graus voce gostaria de girar o cubo:"))
    pi = math.pi
    angulo = angulo1 * ( pi / 180 )

    p1x0 = p1x - 250
    p1y0 = p1y - 250
    p2x0 = p2x - 250
    p2y0 = p2y - 250
    p3x0 = p3x - 250
    p3y0 = p3y - 250
    p4x0 = p4x - 250
    p4y0 = p4y - 250
    calculos(p1x0, p1y0, p2x0, p2y0, p3x0, p3y0, p4x0, p4y0, angulo)
    return p1x0, p1y0, p2x0, p2y0, p3x0, p3y0, p4x0, p4y0, angulo

def calculos (p1x0, p1y0, p2x0, p2y0, p3x0, p3y0, p4x0, p4y0, angulo):
    cos = math.cos(angulo)
    sen = math.sin(angulo)

    p1x = (p1x0 * cos - (p1y0 * sen)) + 250
    p2x = (p2x0 * cos - (p2y0 * sen)) + 250
    p3x = (p3x0 * cos - (p3y0 * sen)) + 250
    p4x = (p4x0 * cos - (p4y0 * sen)) + 250

    p1y = (p1y0 * cos + (p1x0 * sen)) + 250
    p2y = (p2y0 * cos + (p2x0 * sen)) + 250
    p3y = (p3y0 * cos + (p3x0 * sen)) + 250
    p4y = (p4y0 * cos + (p4x0 * sen)) + 250

    desenho(p1x, p1y, p2x, p2y, p3x, p3y, p4x, p4y)
    return p1x, p1y, p2x, p2y, p3x, p3y, p4x, p4y

inicio()
