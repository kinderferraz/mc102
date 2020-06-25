# -*- coding: utf-8 -*-
# Tarefa de laboratório 7 -- Médias de MC102
# Alkindar Ferraz Rodrigues -- 154532


def tuplasLab(x):
    x = x[1:-1]  # remove parênteses
    x = x.split(",")  # separa em duas strings
    f = float(x[0])  # converte primeiro elemento para float
    i = int(x[1])  # converte segundo elemento para int
    return (f, i)  # retorna tupla


# Receber valores de entrada
atividadesConceituais = [float(x) for x in input().split()]
labs = [tuplasLab(x) for x in input().split()]
provas = [float(x) for x in input().split()]
freq = int(input())

# Calcular média das atividades atividades conceituais
mediaAtv = 0
for nota in atividadesConceituais:
    mediaAtv += nota
mediaAtv /= len(atividadesConceituais)

# Calcular média das tarefas de laboratórios
mLab = 0
notas = 0
pesos = 0

for item in labs:
    nota, peso = item
    notas += nota * peso
    pesos += peso
mLab = notas / pesos

# Calcular média das provas
mProvas = (provas[0] * 2 + provas[1] * 3) / 5

# Calcular média preliminar
mPon = 0.6 * mProvas + 0.3 * mLab + 0.1 * mediaAtv
mPre = min(mProvas, mLab, mPon)

# Imprimir as saidas
print("Média das atividades conceituais:", format(mediaAtv, ".1f"))
print("Média das tarefas de laboratório:", format(mLab, ".1f"))
print("Média das provas:", format(mProvas, ".1f"))
print("Média ponderada dos elementos:", format(mPon, ".1f"))
print("Média preliminar:", format(mPre, ".1f"))
if freq >= 75:
    if mPre > 5:
        print("Aprovado(a) por nota e frequência.")
        print("Média final:", format(mPon, ".1f"))
    elif 2.5 < mPre < 5:
        exame = float(input())
        print("Nota no exame:", format(exame, ".1f"))
        mFin = (mPre + exame) / 2
        if mFin >= 5:
            print("Aprovado(a) por nota e frequência.")
            print("Média final:", format(mFin, ".1f"))
        else:
            print("Reprovado(a) por nota.")
            print("Média final:", format(mFin, ".1f"))
    else:
        print("Reprovado(a) por nota.")
        print("Média final:", format(mPre, ".1f"))
else:
    print("Reprovado(a) por frequência.")
    print("Média final:", format(mPre, ".1f"))
