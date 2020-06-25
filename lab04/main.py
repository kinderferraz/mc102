# -*- coding: utf-8 -*-
#   Alkindar Jose Ferraz Rodrigues --- 154532
#   MC102 -- O


# <codecell>
# Ler as informações do aquivo .in
tipo = input()
base = int(input())
car = input()

# determinar se a base é valida
if (base % 2 == 0):
    print("Base inválida.")
    quit()


# definir uma função para cada forma desejada
def TR():
    for j in range(1, base + 1, 2):
        print(j * car)


def TRI():
    for j in range(base, 0, -2):
        print(j * car)


def TI():
    j = base - (base // 2 + 1)
    for i in range(1, base + 1, 2):
        print(' ' * j + car * (i))
        j -= 1


def TII():
    j = 0
    for i in range(base, 0, -2):
        print(' ' * j + car * (i))
        j += 1


def A():
    j = 0
    for i in range(base, 1, -2):
        print(' ' * j + car * (i))
        j += 1

    j = base - (base // 2 + 1)
    for i in range(1, base + 1, 2):
        print(' ' * j + car * (i))
        j -= 1


# para a forma estrela, combinação das anteriores, o codigo foi reutilizado
# quando possivel, e separado segundo as partes da forma
def E():
    # topo da estrela
    j = (base + base//2)
    for i in range(1, base, 2):
        print(' ' * j + car * (i))
        j -= 1

    # linha que divide em 1/3
    print((base * 3) * car)

    # lado de cima da ampulheta
    j = 1
    k = base + 2
    for i in range(base-2, 1, -2):
        print(' ' * j + car * (i) + k * " " + car * (i))
        j += 1
        k += 2

    # lado de baixo da ampulheta
    j = base - (base // 2 + 1)
    k = (base * 2) - 1
    for i in range(1, base, 2):
        print(' ' * j + car * (i) + k * " " + car * (i))
        j -= 1
        k -= 2

    # linha que divide em 2/3
    print((base * 3) * car)

    # ponta de baixo da estrela
    j = base + 1
    for i in range(base-2, 0, -2):
        print(' ' * j + car * (i))
        j += 1


# <codecell>
# exibir a forma com base no tipo determinado pelo arq.in
if tipo == "TR":
    TR()
elif tipo == "TRI":
    TRI()
elif tipo == "TI":
    TI()
elif tipo == "TII":
    TII()
elif tipo == "A":
    A()
elif tipo == "E":
    E()
else:
    print("Objeto inválido.")
