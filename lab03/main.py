# -*- coding: utf-8 -*-

# Tarefa de MC102 -- Lab 03
# nome: alkindar rodrigues
# ra: 154532
# testando triangulos

lado1 = float(input())
lado2 = float(input())
lado3 = float(input())

# ordenar os valores em ordem decrescente:
if lado2 > lado1:
    lado1, lado2 = lado2, lado1
if lado3 > lado1:
    lado1, lado3 = lado3, lado1
if lado3 > lado2:
    lado2, lado3 = lado3, lado2

# triangulos validos se e somente se
ex1 = abs(lado2 - lado3) < lado1 < lado2 + lado3
ex2 = abs(lado1 - lado3) < lado2 < lado1 + lado3
ex3 = abs(lado1 - lado2) < lado3 < lado1 + lado2

# testes lógicos para determinar o tipo do triangulo segundo os lados

l12 = lado1 == lado2
l23 = lado2 == lado3
l13 = lado1 == lado3

if l13 and l23 and l13:
    tipo_lado = "Triângulo equilátero."
elif l12 or l23 or l13:
    tipo_lado = "Triângulo isósceles."
else:
    tipo_lado = "Triângulo escaleno."

# testes lógicos para determinar o tipo do triângulo segundo os angulos

if lado1**2 < (lado2**2 + lado3**2):
    tipo_angulo = "Triângulo acutângulo."
elif lado1**2 == (lado2**2 + lado3**2):
    tipo_angulo = "Triângulo retângulo."
else:
    tipo_angulo = "Triângulo obtusângulo."

if not (ex1 or ex2 or ex3):
    print("Valores inválidos na entrada.")
else:
    print(tipo_lado)
    print(tipo_angulo)
