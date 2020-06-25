# -*- coding: utf-8 -*-
# Tarefa de laboratório 06
# Alkindar Ferraz Rodrigues — 154532

# Ler o numero de casos, testar se o valor é valido
qtosCasos = int(input())
if (1 >= qtosCasos >= 100):
    print("Valor inválido na entrada.")
    quit()

# Iniciar uma lista de casos, um conjunto de pessoas, um dicionario de
# assassinos e detetives e uma lista de mortos
casos = []
pessoas = set()
assassinos = {}
detetives = {}
mortos = []

# ler cada caso
for i in range(qtosCasos):
    assassino, vitima, detetive = input().split()
    caso = {}
    # Colocar todas as pessoas numa lista geral de casos
    casos.append(caso)
    caso["assassino"] = assassino
    caso["vitima"] = vitima
    caso["detetive"] = detetive
    # Colocar todos num grupo
    pessoas.add(assassino)
    pessoas.add(vitima)
    pessoas.add(detetive)
    # Colocar os assassinos, vitimas e detetives em dicionarios para cada papel
    # com quantas vezes cada um atou no papel
    if assassino not in assassinos:
        assassinos[assassino] = {"total": 1}
    else:
        assassinos[assassino]["total"] += 1

    # Adicionar a vitima a uma lista e o detetive a um dicionario
    if vitima not in mortos:
        mortos.append(vitima)

    if detetive not in detetives:
        detetives[detetive] = 1
    else:
        detetives[detetive] += 1

    # Criar chaves de controle para quando se mata um assassino ou detetive
    assassinos[assassino]["matouAssasinos"] = 0
    assassinos[assassino]["matouDetetives"] = 0
    assassinos[assassino]["matouInocentes"] = 0

# Adicionar a especificação de mortos, caso forem assassinos ou detetives
for vitima in mortos:
    for i in range(qtosCasos):
        if casos[i]["vitima"] == vitima:
            assassino = casos[i]["assassino"]
            if vitima in detetives:
                assassinos[assassino]["matouDetetives"] += 1
            elif vitima in assassinos:
                assassinos[assassino]["matouAssasinos"] += 1
            else:
                assassinos[assassino]["matouInocentes"] += 1

print(60 * "-")
for pessoa in sorted(pessoas):
    # relatório com a expressão "in memoriam":
    if pessoa in mortos:
        if pessoa in detetives:
            print(pessoa, "(in memoriam): detetive.")
            print("  Resolveu", detetives[pessoa], "caso(s).")
            if pessoa in assassinos and assassinos[pessoa][
                    "matouDetetives"] > 0:
                print("        Matou", assassinos[pessoa]["matouDetetives"],
                      "detetives.")
            if pessoa in assassinos and assassinos[pessoa][
                    "matouAssasinos"] > 0:
                print("  Matou", assassinos[pessoa]["matouAssasinos"],
                      "assassino(s).")
            if pessoa in assassinos and assassinos[pessoa][
                    "matouInocentes"] > 0:
                print("  Matou", assassinos[pessoa]["matouInocentes"],
                      "inocente(s).")

        elif pessoa in assassinos:
            print(pessoa, "(in memoriam): assassino(a).")
            if assassinos[pessoa]["matouDetetives"] > 0:
                print("    Matou", assassinos[pessoa]["matouDetetives"],
                      "detetive(s).")
            if assassinos[pessoa]["matouAssasinos"] > 0:
                print("    Matou", assassinos[pessoa]["matouAssasinos"],
                      "assassino(s).")
            if assassinos[pessoa]["matouInocentes"] > 0:
                print("    Matou", assassinos[pessoa]["matouInocentes"],
                      "inocente(s).")

        else:
            print(pessoa, "(in memoriam): vítima inocente.")
    # Relatório sem a expressão "in memoriam"
    else:
        if pessoa in detetives:
            print(str(pessoa) + ": detetive.")
            print("  Resolveu", detetives[pessoa], "caso(s).")

            if pessoa in assassinos and assassinos[pessoa][
                    "matouDetetives"] > 0:
                print("  Matou", assassinos[pessoa]["matouDetetives"],
                      "detetive(s).")

            if pessoa in assassinos and assassinos[pessoa][
                    "matouAssasinos"] > 0:
                print("  Matou", assassinos[pessoa]["matouAssasinos"],
                      "assassino(s).")

            if pessoa in assassinos and assassinos[pessoa][
                    "matouInocentes"] > 0:
                print("  Matou", assassinos[pessoa]["matouInocentes"],
                      "inocente(s).")

        elif pessoa in assassinos:
            print(str(pessoa) + ": assassino(a).")
            if assassinos[pessoa]["matouDetetives"] > 0:
                print("  Matou", assassinos[pessoa]["matouDetetives"],
                      "detetive(s).")
            if assassinos[pessoa]["matouAssasinos"] > 0:
                print("  Matou", assassinos[pessoa]["matouAssasinos"],
                      "assassino(s).")
            if assassinos[pessoa]["matouInocentes"] > 0:
                print("  Matou", assassinos[pessoa]["matouInocentes"],
                      "inocente(s).")
    # se a pessoa está viva nao pode ser vitima, logo nao possui a expressão
    print(60 * "-")
